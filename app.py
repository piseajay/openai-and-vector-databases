import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.Client()
default_embedding = embedding_functions.DefaultEmbeddingFunction()

collection_name = "tets-collection"
collection = chroma_client.get_or_create_collection(name=collection_name,embedding_function=default_embedding)

documents = [
    {"id": "doc1" , "text":"Hello, World!"},
    {"id": "doc2" , "text":"How are you?"},
    {"id": "doc3" , "text":"Goodbye, see you later!"},
    {"id": "doc4" , "text":"Hello, Earth!"}
]

for doc in documents:
    collection.upsert(ids=[doc["id"]], documents=[doc["text"]])

query = "Hello, World!"

result = collection.query(query_texts=[query], n_results=4)
print(result)
