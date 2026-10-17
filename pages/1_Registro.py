import streamlit as st

from auth import get_authenticator
from mensajes import traducir

st.set_page_config(page_title="Registro", page_icon="📝")

authenticator = get_authenticator()

st.title("Darme de alta")

try:
    email, username, name = authenticator.register_user(
        location="main",
        # Sin pre_authorized -> registro abierto.
        # Para invitación, descomentá el bloque pre-authorized en config.yaml.
        password_hint=False,  # oculta el campo "pista de contraseña"
        captcha=True,
        fields={
            "Form name": "Crear cuenta",
            "First name": "Nombre",
            "Last name": "Apellido",
            "Email": "Correo",
            "Username": "Usuario",
            "Password": "Contraseña",
            "Repeat password": "Repetir contraseña",
            "Captcha": "Código de la imagen",
            "Register": "Registrarme",
        },
    )
    if email:
        st.success(f"Usuario **{username}** registrado correctamente.")
        st.info("Volvé a la página principal para iniciar sesión.")
except Exception as error:
    st.error(traducir(error))

st.caption(
    "La contraseña debe tener 8-20 caracteres, con mayúscula, minúscula, "
    "número y un símbolo."
)
