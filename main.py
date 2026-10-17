import streamlit as st

from auth import get_authenticator

st.set_page_config(page_title="Login", page_icon="🔐")

authenticator = get_authenticator()

# En 0.4.x login() con location='main' NO devuelve tupla: renderiza el form
# y deja el resultado en st.session_state.
authenticator.login(
    location="main",
    fields={
        "Form name": "Iniciar sesión",
        "Username": "Usuario",
        "Password": "Contraseña",
        "Login": "Entrar",
    },
)

status = st.session_state.get("authentication_status")

if status:
    st.title("Ya estás dentro")
    st.write(f"Bienvenid@ *{st.session_state.get('name')}*")
    authenticator.logout("Cerrar sesión", "sidebar")
elif status is False:
    st.error("Usuario o contraseña incorrectos.")
else:
    st.warning("Introduzca su usuario y contraseña.")
