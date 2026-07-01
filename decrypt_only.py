# Saurabh - Decrypt Tool
# Bas ye file run karo, encrypted message aur password dalo.
import hashlib, hmac, base64

ITERATIONS = 100_000

def _derive_key(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, ITERATIONS, dklen=32)

def _xor(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def decrypt(enc_b64, password):
    try:
        payload = base64.b64decode(enc_b64.encode())
    except Exception:
        raise ValueError("Invalid format.")
    if len(payload) < 48:
        raise ValueError("Corrupted message.")

    salt, mac, ciphertext = payload[:16], payload[16:48], payload[48:]
    key = _derive_key(password, salt)

    if not hmac.compare_digest(hmac.new(key, ciphertext, hashlib.sha256).digest(), mac):
        raise ValueError("Wrong password or message has been tampered.")

    return _xor(ciphertext, key).decode('utf-8')


print("=" * 50)
print("   Saurabh - Decrypt Tool")
print("=" * 50)
enc = input("\nEnter encrypted message: ").strip()
pwd = input("Enter password/key: ")
try:
    print(f"\nDecrypted : {decrypt(enc, pwd)}")
except ValueError as e:
    print(f"\n❌ {e}")