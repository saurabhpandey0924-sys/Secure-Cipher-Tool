import hmac
import hashlib
import base64
from core.keygen import generate_salt, derive_key

def _xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def encrypt_message(plaintext: str, password: str) -> str:
    salt = generate_salt()
    key = derive_key(password, salt)

    ciphertext = _xor(plaintext.encode('utf-8'), key)
    mac = hmac.new(key, ciphertext, hashlib.sha256).digest()

    # Format: [16 bytes salt][32 bytes HMAC][ciphertext]
    payload = salt + mac + ciphertext
    return base64.b64encode(payload).decode('utf-8')