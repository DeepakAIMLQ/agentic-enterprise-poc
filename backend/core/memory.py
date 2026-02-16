# backend/core/memory.py
import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()

embedding_fn = embedding_functions.DefaultEmbeddingFunction()

collection = client.get_or_create_collection(
    name="agentic_memory",
    embedding_function=embedding_fn
)

def save_memory(id: str, text: str, metadata: dict = {}):
    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[id]
    )

def query_memory(query: str, n_results=3):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results["documents"][0] if results["documents"] else []
