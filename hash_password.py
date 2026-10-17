"""Genera un hash bcrypt para pegar en config.yaml.

Uso:  python hash_password.py "MiClave123!"
"""

import sys

import bcrypt

if len(sys.argv) != 2:
    sys.exit('Uso: python hash_password.py "MiClave123!"')

print(bcrypt.hashpw(sys.argv[1].encode(), bcrypt.gensalt()).decode())
