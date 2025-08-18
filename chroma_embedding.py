from chromadb.utils import embedding_functions

default_embedding = embedding_functions.DefaultEmbeddingFunction()

name = "Ajay Pise"

embeddings = default_embedding(name)

print(embeddings)