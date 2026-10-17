"""
Traducción de los mensajes de error de streamlit-authenticator, que vienen
en inglés desde la librería.
"""

ERRORES = {
    "Email already taken": "Ese correo ya está registrado.",
    "Username/email already taken": "Ese usuario ya está en uso.",
    "User already exists": "El usuario ya existe.",
    "User not pre-authorized to register":
        "Tu correo no está en la lista de invitados.",
    "First name is not valid": "El nombre no es válido.",
    "Last name is not valid": "El apellido no es válido.",
    "Email is not valid": "El correo no es válido.",
    "Email domain is not allowed to register":
        "El dominio de ese correo no está permitido.",
    "Username is not valid":
        "El usuario no es válido (hasta 20 caracteres: letras, números, _ o -).",
    "Username not provided": "Falta el usuario.",
    "Email not provided": "Falta el correo.",
    "Passwords do not match": "Las contraseñas no coinciden.",
    "Password/repeat password fields cannot be empty":
        "Tenés que completar la contraseña y su repetición.",
    "Password hint cannot be empty": "La pista de contraseña no puede estar vacía.",
    "New and current passwords are the same":
        "La contraseña nueva es igual a la actual.",
    "No new password provided": "No ingresaste una contraseña nueva.",
    "Captcha not entered": "Tenés que escribir el código de la imagen.",
    "Captcha entered incorrectly": "El código de la imagen es incorrecto.",
    "Maximum number of login attempts exceeded":
        "Superaste el máximo de intentos de inicio de sesión.",
    "Maximum number of concurrent users exceeded":
        "Se superó el máximo de usuarios conectados a la vez.",
    "Cannot log in multiple sessions":
        "No podés iniciar sesión en varias sesiones a la vez.",
    "User not authorized": "Usuario no autorizado.",
}

# El diagnóstico de contraseña llega como un texto armado por partes.
FRAGMENTOS = {
    "**Password must:**": "**La contraseña debe:**",
    "Between 8 and 20 characters long": "Tener entre 8 y 20 caracteres",
    "Contain at least one lowercase letter": "Tener al menos una minúscula",
    "Contain at least one uppercase letter": "Tener al menos una mayúscula",
    "Contain at least one digit": "Tener al menos un número",
    "Contain at least one special character (@$!%*?&)":
        "Tener al menos un símbolo (@$!%*?&)",
}


def traducir(error) -> str:
    texto = str(error)
    if texto in ERRORES:
        return ERRORES[texto]
    for ingles, espanol in FRAGMENTOS.items():
        texto = texto.replace(ingles, espanol)
    return texto
