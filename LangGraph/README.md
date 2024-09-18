# LangGraph - Sistema de Preguntas y Respuestas Basado en Grafos

Este proyecto implementa un sistema de **Preguntas y Respuestas** utilizando **LangGraph** y **NetworkX** para representar la información en forma de grafo. Las respuestas se generan utilizando el modelo **GPT-2** de Hugging Face, con contexto basado en la estructura del grafo.

## Requisitos

- Python 3.7+
- LangGraph
- NetworkX
- Hugging Face Transformers
- PyTorch

### Instalación

1. Clona este repositorio.
2. Instala las dependencias necesarias ejecutando:

    ```bash
    pip install langgraph transformers networkx torch
    ```

### Uso del Sistema

Para ejecutar el sistema de preguntas y respuestas, simplemente corre el script principal:

```bash
python langgraph_example.py
```

Una vez que se ejecute el script, se le pedirá una pregunta. Puedes escribir "salir" para terminar el programa. La respuesta se generará utilizando el modelo **GPT-2** y se mostrará en la consola.