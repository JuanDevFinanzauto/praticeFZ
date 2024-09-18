# FastAPI Example

Este proyecto es un ejemplo básico de una API REST creada con **FastAPI**. Incluye algunas rutas para obtener y crear ítems, y está estructurado de manera simple para dar continuidad al tutorial de usar FastAPI.

## Requisitos

Asegúrate de tener instalado [Python 3.7+](https://www.python.org/downloads/) en tu máquina antes de empezar.

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias:

    ```bash
    pip install fastapi uvicorn
    ```

## Estructura del proyecto

- **`main.py`**: Es el archivo principal de la aplicación FastAPI donde se definen las rutas y modelos.
- **FastAPI**: Un framework moderno y rápido para construir APIs con Python 3.7+ basado en estándares como OpenAPI y JSON Schema.
- **Pydantic**: Se utiliza para validar y gestionar los datos entrantes a través de modelos definidos.

## Ejecución del servidor

Una vez instaladas las dependencias, puedes ejecutar la aplicación localmente utilizando Uvicorn como servidor ASGI:

```bash
uvicorn main:app --reload
