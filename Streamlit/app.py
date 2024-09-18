import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Mi primera aplicación con Streamlit')

x_value = st.slider('Selecciona un valor para X', 0, 100, 50)

x = np.linspace(0, 100, 500)
y = x_value * np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)
