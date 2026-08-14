"""
Converts each text chunk into a numeric embedding using a sentence
transformer model.
"""

from sentence_transformers import SentenceTransformer

# Reuse the exact same chunking code from Step 1
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
    
    chunks = chunk_text(sample_document, chunk_size=30)
    print(f"We have {len(chunks)} chunks.\n")

    print("Loading the embedding model... (first run may take a minute)")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    embeddings = model.encode(chunks)

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        print(f"--- Chunk {i+1} ---")
        print(f"Text: {chunk[:60]}...")  # just show first 60 characters
        print(f"Embedding: a list of {len(embedding)} numbers")
        print(f"First 5 numbers as a preview: {embedding[:5]}")
        print()

    print("Done! Each chunk now has its own numeric fingerprint.")