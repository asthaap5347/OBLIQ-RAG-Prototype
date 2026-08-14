"""
Embeds each chunk and stores it in Supabase (pgvector) for later retrieval.
"""

from sentence_transformers import SentenceTransformer
from supabase import create_client
from dotenv import load_dotenv          
import os                                

load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


# Same sample document + chunking function as before
sample_document = """
Obliq-io is an AI-powered automation platform designed for CA (Chartered
Accountant) firms. It helps automate repetitive tasks like data entry,
compliance checks, and report generation.

The platform uses AI agents to read financial documents, extract key
information, and flag inconsistencies automatically. This saves accountants
hours of manual review time every week.

Obliq-io also offers a workflow builder, allowing firms to design custom
automation pipelines without writing code. Users can drag and drop steps
like "extract data," "validate," and "generate report."

Security is a top priority for Obliq-io. All documents are encrypted at
rest and in transit, and the platform is built to comply with financial
data regulations.
"""

def chunk_text(text, chunk_size=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk_words = words[i:i + chunk_size]
        chunks.append(" ".join(chunk_words))
    return chunks


if __name__ == "__main__":
   
    print("Connecting to Supabase...")
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    chunks = chunk_text(sample_document, chunk_size=30)
    print(f"We have {len(chunks)} chunks.")

    print("Creating embeddings...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)

    print("Saving to Supabase...")
    for chunk, embedding in zip(chunks, embeddings):
        supabase.table("documents").insert({
            "content": chunk,
            "embedding": embedding.tolist()  # convert to a plain list of numbers
        }).execute()

    print(f"\nDone! Saved {len(chunks)} chunks to your Supabase database.")
    print("Go check your 'documents' table in Supabase - you should see them there!")