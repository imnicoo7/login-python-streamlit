"""
Fábrica única del objeto Authenticate.

Se importa desde main.py y desde las páginas de pages/.
Al pasar la RUTA del config.yaml (y no el dict), streamlit-authenticator 0.4.x
persiste solo los cambios (registro de usuarios, reset de password, etc.);
por eso NO hay que hacer yaml.dump a mano.
"""

from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

CONFIG_PATH = Path(__file__).parent / "config.yaml"


def load_config() -> dict:
    with open(CONFIG_PATH, encoding="utf-8") as file:
        return yaml.load(file, Loader=SafeLoader)


def _secret(name: str, default):
    """st.secrets explota si no existe .streamlit/secrets.toml; lo aislamos."""
    try:
        return st.secrets[name]
    except Exception:
        return default


def get_authenticator() -> stauth.Authenticate:
    config = load_config()
    cookie = config["cookie"]

    # La clave firma el JWT de la cookie. En producción va en
    # .streamlit/secrets.toml (cookie_key = "..."), nunca en el repo.
    cookie_key = _secret("cookie_key", cookie["key"])

    return stauth.Authenticate(
        str(CONFIG_PATH),  # ruta -> la librería guarda los cambios sola
        cookie["name"],
        cookie_key,
        cookie["expiry_days"],
    )


def get_preauthorized_emails() -> list:
    config = load_config()
    block = config.get("pre-authorized") or config.get("preauthorized") or {}
    return block.get("emails") or []
