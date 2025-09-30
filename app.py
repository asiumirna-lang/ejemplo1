import streamlit as st
import random

st.title("🎯 Resolviendo ecuaciones de primer grado")

# Generar coeficientes aleatorios
a = random.randint(1, 10)
b = random.randint(1, 20)

# Ecuación: ax + b = 0
st.write(f"Resuelve la siguiente ecuación: **{a}x + {b} = 0**")

# Respuesta correcta
correcta = -b / a

# Campo para ingresar la respuesta
respuesta = st.number_input("Escribe tu respuesta para x:", step=1.0)

# Botón para verificar
if st.button("Verificar"):
    if respuesta == correcta:
        st.success("✅ ¡Correcto! 🎉")
        st.balloons()
    else:
        st.error("❌ Incorrecto, intenta otra vez.")
