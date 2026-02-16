import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()
embedding_fn = embedding_functions.DefaultEmbeddingFunction()

# Use get_or_create_collection WITHOUT passing embedding_fn as second param
try:
    collection = client.get_collection("agentic_memory")
    print("✓ Collection exists")
except:
    collection = client.create_collection("agentic_memory", embedding_function=embedding_fn)
    print("✓ Collection created")

print(f"Total vectors: {collection.count()}")

if collection.count() == 0:
    print("No vectors saved yet. Run your pipeline first!")
else:
    all_results = collection.get()
    print("\nIDs:", all_results.get("ids", []))
    print("Documents:", all_results.get("documents", []))
    print("Metadata:", all_results.get("metadatas", []))

    # Test query
    query_results = collection.query(query_texts=["BRD"], n_results=3)
    print("\nQuery matches:", query_results)
