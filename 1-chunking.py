"""
Splits a document into smaller text chunks so they can be embedded
and searched individually.
"""

# This is our sample document for now.

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
    """
    Splits text into chunks of roughly `chunk_size` words each.

    text: the full document (a string)
    chunk_size: how many words per chunk (200 is a good starting point)
    """
    
    words = text.split()

    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk_words = words[i:i + chunk_size]
        chunk_text_piece = " ".join(chunk_words)
        chunks.append(chunk_text_piece)

    return chunks


if __name__ == "__main__":
    # Run the chunking function on our sample document
    chunks = chunk_text(sample_document, chunk_size=30)  # small size just so we get multiple chunks to see

    print(f"Document was split into {len(chunks)} chunks.\n")

    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ---")
        print(chunk)
        print()