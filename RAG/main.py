import torch
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
from datasets import load_dataset
import faiss

dataset = load_dataset("csv", data_files="data/documents.csv")

tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_name="exact", passages_path="data/passages")
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)

def query_rag_system(question):
    input_ids = tokenizer(question, return_tensors="pt")["input_ids"]

    outputs = model.generate(input_ids, num_return_sequences=1, num_beams=2)
    
    answer = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    
    return answer

if __name__ == "__main__":
    while True:
        question = input("Haz una pregunta: ")
        if question.lower() == "salir":
            break
        response = query_rag_system(question)
        print(f"Respuesta: {response}")
