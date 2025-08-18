import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types import CreateEmbeddingResponse

load_dotenv()

def create_embeddings(input:str) -> CreateEmbeddingResponse:
    return client.embeddings.create(input=input,model="text-embedding-3-small")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = create_embeddings(input="Red")
response1 = create_embeddings(input="Orange")
print(response, response1)