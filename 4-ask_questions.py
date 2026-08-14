"""
Given a question, retrieves the most relevant chunks from Supabase
and uses Gemini to answer based on that context.
"""

from sentence_transformers import SentenceTransformer
from supabase import create_client
import google.generativeai as genai
from dotenv import load_dotenv         
import os                               

load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Connect to everything
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
genai.configure(api_key=GEMINI_API_KEY)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
gemini_model = genai.GenerativeModel('gemini-flash-latest')


def answer_question(question):
    
    question_embedding = embedding_model.encode(question).tolist()

    result = supabase.rpc('match_documents', {
        'query_embedding': question_embedding,
        'match_count': 4
    }).execute()

    matched_chunks = result.data
    print(f"\nFound {len(matched_chunks)} relevant chunks:")
    for chunk in matched_chunks:
        print(f"  - (similarity: {chunk['similarity']:.2f}) {chunk['content'][:70]}...")

    context = "\n\n".join([chunk['content'] for chunk in matched_chunks])

    prompt = f"""Answer the question using ONLY the information in the context below.
If the answer isn't in the context, say "I don't have enough information to answer that."

Context:
{context}

Question: {question}

Answer:"""

    response = gemini_model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    print("=" * 50)
    print("Ask a question about Obliq-io (type 'quit' to stop)")
    print("=" * 50)

    while True:
        question = input("\nYour question: ")
        if question.lower() == "quit":
            break

        answer = answer_question(question)
        print(f"\nAnswer: {answer}")
