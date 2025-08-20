import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

load_dotenv()
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(pinecone_api_key)

pc.create_index(
    name="quickstart",
    dimension=17,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1"),
)
