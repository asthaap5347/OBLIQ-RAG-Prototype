# OBLIQ-RAG-Prototype

A Retrieval-Augmented Generation (RAG) prototype developed as part of the OBLIQ.io evaluation task.

The prototype demonstrates a complete document-to-question-answering pipeline using text chunking, semantic embeddings, Supabase storage, and Google Gemini.

## Overview

This project explores how an AI system can retrieve relevant information from a document and use that information to generate context-aware answers.

The current pipeline is:

Document  
↓  
Text Chunking  
↓  
Semantic Embeddings  
↓  
Supabase Storage  
↓  
Relevant Context Retrieval  
↓  
Gemini  
↓  
Answer

## Tech Stack

- Python
- Sentence Transformers
- Supabase
- Google Gemini API
- python-dotenv

## Project Structure

```text
OBLIQ-RAG-Prototype/
│
├── 1-chunking.py
├── 2-embeddings.py
├── 3-storing.py
├── 4-ask_questions.py
├── .gitignore
└── README.md

## Purpose

This project was built as an individual prototype for the OBLIQ.io evaluation task, with a focus on understanding and implementing the core components of a Retrieval-Augmented Generation system.
