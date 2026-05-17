from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings


def initialize_gemma_llm():
    return Ollama(model="gemma4:e4b")

def setup_embedding_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#from langchain_community.embeddings import OllamaEmbeddings
#OllamaEmbeddings(model="nomic-embed-text")