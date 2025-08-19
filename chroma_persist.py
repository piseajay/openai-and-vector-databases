import chromadb
from chromadb.utils import embedding_functions

default_ef = embedding_functions.DefaultEmbeddingFunction()
chroma_clinet = chromadb.PersistentClient(path="./db/chroma_persist")

collection = chroma_clinet.get_or_create_collection(
    "my_collection", embedding_function=default_ef
)

documents = [
    {"id": "doc1", "text": "Hello, World!"},
    {"id": "doc2", "text": "How are you?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
    {
        "id": "doc4",
        "text": "Microsoft is a multinational technology company known for its software, services, and hardware products. Founded in 1975, it's a leading force in the tech industry, particularly in personal computer software with operating systems like Windows. Beyond Windows, Microsoft also offers cloud computing services (Azure), productivity software (Microsoft 365), gaming (Xbox), and other online services.",
    },
    {
        "id": "doc5",
        "text": "Elon Reeve Musk FRS is a businessman, known for his leadership of Tesla, SpaceX, X, and the Department of Government Efficiency. Musk has been the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion.",
    },
]

for doc in documents:
    collection.upsert(ids=[doc["id"]], documents=[doc["text"]])

query_text = "Best Technology company?"

result = collection.query(query_texts=query_text, n_results=1)

print(result)
