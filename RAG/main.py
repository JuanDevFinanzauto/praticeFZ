from transformers import pipeline, RagTokenizer, RagRetriever, RagSequenceForGeneration
import pandas as pd
from datasets import Dataset

# Cargar los documentos desde un CSV a un dataset Hugging Face compatible
# Asegúrate de que el archivo documents.csv tiene una columna "text" con los documentos
data = pd.read_csv("data/documents.csv")
dataset = Dataset.from_pandas(data)

# Inicializar el tokenizer y el modelo RAG
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")

# Configurar el retriever usando una opción básica y menos dependiente de código remoto
retriever = RagRetriever.from_pretrained(
    "facebook/rag-token-nq", 
    index_name="legacy",
    use_dummy_dataset=True  # Utiliza un dataset dummy para simplificar el ejemplo
)

# Inicializar el modelo RAG para generación de secuencias
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)

# Definir una función para hacer consultas al sistema RAG
def query_rag_system(question):
    input_ids = tokenizer(question, return_tensors="pt")["input_ids"]
    outputs = model.generate(input_ids)
    answer = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    return answer

# Ejecutar el sistema RAG en modo interactivo
if __name__ == "__main__":
    while True:
        question = input("Haz una pregunta (o escribe 'salir' para terminar): ")
        if question.lower() == "salir":
            break
        response = query_rag_system(question)
        print(f"Respuesta: {response}")
