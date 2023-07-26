import streamlit as st
from main import authenticator
try:
    if authenticator.register_user('Darme de alta', preauthorization=False):
        st.success('Usuario registrado correctamente')
except Exception as e:
    st.error(e)
