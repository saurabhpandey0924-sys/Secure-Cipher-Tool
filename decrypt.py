import hmac
import hashlib
import base64
from core.keygen import derive_key

def _xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def decrypt_message(encrypted_b64: str, password: str) -> str:
    try:
        payload = base64.b64decode(encrypted_b64.encode('utf-8'))
    except Exception:
        raise ValueError("Invalid encrypted text format.")

    if len(payload) < 48:
        raise ValueError("Corrupted message.")

    salt       = payload[:16]
    mac        = payload[16:48]
    ciphertext = payload[48:]

    key = derive_key(password, salt)

    # HMAC verify — wrong password ya tampered message toh yahan fail hoga
    expected_mac = hmac.new(key, ciphertext, hashlib.sha256).digest()
    if not hmac.compare_digest(mac, expected_mac):
        raise ValueError("Wrong password or message has been tampered.")

    return _xor(ciphertext, key).decode('utf-8')