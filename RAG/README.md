# Proyecto RAG - Sistema de Preguntas y Respuestas basado en Documentos

Este proyecto implementa un sistema básico de **Retrieval-Augmented Generation (RAG)** utilizando el modelo `facebook/rag-token-nq` de Hugging Face. El sistema permite realizar preguntas, buscar en una base de documentos y generar respuestas basadas en los documentos recuperados.

## Requisitos

- Python 3.7+
- Hugging Face Transformers
- datasets
- Faiss
- PyTorch

### Instalación

1. Clona este repositorio.
2. Instala las dependencias necesarias ejecutando:

    ```bash
    pip install transformers datasets faiss-cpu torch
    ```

3. Asegúrate de tener un conjunto de documentos almacenados en un archivo CSV. El archivo debe estar en la carpeta `data/` y debe tener al menos una columna con el contenido de los documentos.

### Uso del Sistema

Para ejecutar el sistema de preguntas y respuestas, simplemente corre el script principal:

```bash
python rag_example.py
```

Este script cargará el conjunto de documentos almacenado en el archivo `data/documents.csv` y mostrará una pregunta al usuario. Una vez que se responda la pregunta, el sistema buscará el documento con la informacion proporcionada y generará una respuesta de finanzauto basada en ese documento.