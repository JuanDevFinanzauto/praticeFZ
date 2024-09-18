# Aplicación Web Interactiva con Streamlit

Este proyecto es un ejemplo básico de una aplicación web interactiva construida con **Streamlit**. La aplicación permite al usuario controlar un parámetro mediante un control deslizante y visualizar una gráfica que cambia dinámicamente con la entrada seleccionada.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes herramientas y bibliotecas:

- Python 3.7 o superior
- Las bibliotecas necesarias para el proyecto: `streamlit`, `numpy` y `matplotlib`

Puedes instalar las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install streamlit numpy matplotlib
```

## Ejecución del proyecto    

Para ejecutar el proyecto, asegúrate de tener instalado Python 3.7 o superior en tu máquina y ejecuta el siguiente comando en la terminal:

```bash
streamlit run app.py
```

## ¿Qué hace esta aplicación?

La aplicación tiene una interfaz sencilla que incluye:

Control deslizante: Permite al usuario seleccionar un valor para X entre 0 y 100.

Generación de datos: Calcula una función y = X * sin(x) basada en el valor seleccionado en el control deslizante.

Visualización de la gráfica: Muestra un gráfico que cambia dinámicamente a medida que se ajusta el valor del control deslizante.