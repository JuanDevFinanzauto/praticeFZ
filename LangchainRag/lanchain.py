from langchain import HuggingFaceHub, FAISS
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from datasets import load_dataset
import faiss

dataset = load_dataset("csv", data_files="data/documents.csv")['train']

embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_faiss_index(documents):
    texts = [doc['text'] for doc in documents]
    embeddings = embed_model.embed_documents(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return FAISS(index=index, documents=texts, embeddings=embed_model)

index = create_faiss_index(dataset)

generator = HuggingFaceHub(repo_id="facebook/rag-token-nq", model_kwargs={"temperature": 0.1})

qa_chain = RetrievalQA(combine_documents_chain=generator, retriever=index.as_retriever())

def query_langchain_system(question):
    return qa_chain.run(question)

if __name__ == "__main__":
    while True:
        question = input("Haz una pregunta: ")
        if question.lower() == "salir":
            break
        response = query_langchain_system(question)
        print(f"Respuesta: {response}")
