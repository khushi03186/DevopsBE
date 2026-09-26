# utils.py
import bcrypt
from bcrypt import hashpw, gensalt, checkpw
from jose import jwt

algorithm = "HS256"

def hash_password(password: str):
    """Hash a password for storing."""
    salt = gensalt()
    hashed = hashpw(password.encode(), salt)
    return hashed.decode()

def verify_password(provided_password: str, stored_password: str):
    """Verify a stored password against one provided by user"""
    return checkpw(provided_password.encode(), stored_password.encode())

def create_access_token(data: dict, secret_key: str):
    return jwt.encode(data, secret_key, algorithm=algorithm)

def decode_access_token(token: str, secret_key: str):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        return payload
    except Exception:
        return None