import chromadb 
from pprint import pprint 
client = chromadb.Client() 
try:
   collection = client.create_collection("all-my-documents")
   collection = client.create_collection(name="all-my-documents",metadata={"hnsw:space":"cosine"}) 
except:
   print("This document has been created")

print(collection)

collection.add(
    documents=[
        "This is a document about food",
        "This is a document about animal's food",
        "This is a document about cats and dogs",
    ],
    metadatas=[{"topic": "food"}, {"topic": "animal"}, {"topic": "animal"}],
    ids=["doc1", "docs2", "doc3"],
)
'''
collection.add(
    embeddings=[[...]] # fill own embedding here
    documents=[
        "This is a document about food",
        "This is a document about animal's food",
        "This is a document about cats and dogs",
    ],
    metadatas=[{"topic": "food"}, {"topic": "animal"}, {"topic": "animal"}],
    ids=["doc1", "docs2", "doc3"],
)
'''
results = collection.query(
    query_texts=["This is query about animal foods"],
    n_results=5,
    where={"topic": "food"},
)
print(collection)
print(results)
