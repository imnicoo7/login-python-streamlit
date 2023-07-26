import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import streamlit as st

# ----------------------------------------------------------------------------------------------------------------------
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Iniciar Sesión', 'main')

if st.session_state["authentication_status"]:
    st.write(f'Bienvenid@ *{st.session_state["name"]}*')
    st.title('Ya estás dentro')
    authenticator.logout('Logout', 'main')
elif st.session_state["authentication_status"] == False:
    st.error('La combinación de nombre de usuario y contraseña es incorrecta.')
elif st.session_state["authentication_status"] == None:
    st.warning('Introduzca su nombre de usuario y contraseña')

with open('../config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
    