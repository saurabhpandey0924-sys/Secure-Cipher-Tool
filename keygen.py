import hashlib
import os

ITERATIONS = 100_000  # jitna zyada, brute force utna mushkil

def generate_salt() -> bytes:
    return os.urandom(16)  # random 16-byte salt

def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        ITERATIONS,
        dklen=32
    )