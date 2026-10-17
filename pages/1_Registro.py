import streamlit as st

from auth import get_authenticator, get_preauthorized_emails

st.set_page_config(page_title="Registro", page_icon="📝")

authenticator = get_authenticator()

st.title("Darme de alta")

try:
    email, username, name = authenticator.register_user(
        location="main",
        pre_authorized=get_preauthorized_emails() or None,
        captcha=True,
        fields={
            "Form name": "Registro",
            "First name": "Nombre",
            "Last name": "Apellido",
            "Email": "Correo",
            "Username": "Usuario",
            "Password": "Contraseña",
            "Repeat password": "Repetir contraseña",
            "Register": "Registrarme",
            "Captcha": "Captcha",
        },
    )
    if email:
        st.success(f"Usuario **{username}** registrado correctamente.")
        st.info("Volvé a la página principal para iniciar sesión.")
except Exception as error:
    st.error(error)

st.caption(
    "La contraseña debe tener 8-20 caracteres, con mayúscula, minúscula, "
    "número y un símbolo."
)
