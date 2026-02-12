import secrets
import hashlib


def generate_nonce(length: int = 32) -> str:
    """
    Cryptographically secure nonce.
    """
    return secrets.token_hex(length)


def secure_hash(data: str) -> str:
    """
    SHA-256 hashing.
    """
    return hashlib.sha256(data.encode()).hexdigest()
