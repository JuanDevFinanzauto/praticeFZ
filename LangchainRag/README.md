# Langchain RAG - Sistema de Preguntas y Respuestas

Este proyecto implementa un sistema **Retrieval-Augmented Generation (RAG)** utilizando **Langchain**, **FAISS** y **Hugging Face**. El sistema permite realizar preguntas y generar respuestas basadas en un conjunto de documentos cargados desde un archivo CSV.

## Requisitos

- Python 3.7+
- Langchain
- Hugging Face Transformers
- FAISS
- datasets
- PyTorch

### Instalación

1. Clona este repositorio.
2. Instala las dependencias necesarias ejecutando:

    ```bash
    pip install langchain transformers faiss-cpu torch datasets
    ```
    
### Uso del Sistema

Para ejecutar el sistema de preguntas y respuestas, simplemente corre el script principal:

```bash
python langchain_example.py
```

Una vez que se ejecute el script, se le pedirá una pregunta. Puedes escribir "salir" para terminar el programa.