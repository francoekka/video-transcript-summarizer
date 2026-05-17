import os
from langchain_community.vectorstores import FAISS

def create_faiss_index(chunks, embedding_model, persist_path="faiss_index.pkl"):
    if os.path.exists(persist_path):
        return FAISS.load_local(persist_path, embedding_model, allow_dangerous_deserialization=True)
    faiss_index = FAISS.from_texts(chunks, embedding_model)
    faiss_index.save_local(persist_path)
    return faiss_index


def perform_similarity_search(faiss_index, query, k=3):
    return faiss_index.similarity_search(query, k=k)
