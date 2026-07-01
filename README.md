# 🔐 Saurabh — Secure Cipher Tool

A password-based encryption tool built in Python using **PBKDF2-HMAC-SHA256 + XOR + HMAC** — no external libraries required.

---

## 📁 Project Structure

```
saurabh-cipher/
├── cipher.py           # Main tool (encrypt + decrypt)
├── decrypt_only.py     # Lightweight script — share with anyone for decryption
└── core/
    ├── __init__.py
    ├── keygen.py       # PBKDF2 key derivation
    ├── encrypt.py      # Encryption + HMAC logic
    └── decrypt.py      # Decryption + HMAC verification
```

---

## ⚙️ How It Works

```
Password + Random Salt
        │
        ▼
 PBKDF2-HMAC-SHA256         ← 100,000 iterations
 (Key Derivation)
        │
        ▼
   XOR Encryption           ← plaintext XOR derived key
        │
        ▼
   HMAC-SHA256              ← integrity check tag
        │
        ▼
 Base64 Encoded Output      ← shareable encrypted string
```

- **Salt** — 16 random bytes generated per encryption (same message + same password = different output every time)
- **PBKDF2** — 100,000 iterations makes brute force practically impossible
- **HMAC** — wrong password instantly detected, no guessing possible
- **Base64** — encrypted output is a clean, copy-pasteable string

---

## 🚀 Getting Started

No installation needed. Just Python 3.6+.

```bash
git clone https://github.com/< saurabhpandey0924 >/saurabh-cipher.git
cd saurabh-cipher
python cipher.py
```

---

## 📌 Usage

### Main Tool (`cipher.py`)
Run this on your machine to encrypt or decrypt messages.

```
1. Encrypt Message
2. Decrypt Message
3. About Security
4. Exit
```

**Encrypt:**
```
Enter message to encrypt: Hello World
Enter password/key: mysecretpassword

Encrypted : a3F2bX...  (base64 string)
```

**Decrypt:**
```
Enter encrypted message: a3F2bX...
Enter password/key: mysecretpassword

Decrypted : Hello World
```

---

### Sending to a Friend

1. Share `decrypt_only.py` with your friend
2. Send the **encrypted text** (the base64 string)
3. Share the **password separately** (WhatsApp call, in person — never with the encrypted text)

Your friend runs:
```bash
python decrypt_only.py
```
```
Enter encrypted message: a3F2bX...
Enter password/key: mysecretpassword

Decrypted : Hello World
```

> ❌ Wrong password = `Wrong password or message has been tampered.` — no hints, no partial decryption.

---

## 🔒 Security Details

| Property | Detail |
|---|---|
| Algorithm | XOR with PBKDF2-derived key |
| Key Derivation | PBKDF2-HMAC-SHA256 |
| KDF Iterations | 100,000 |
| Salt | 16 bytes (random, per message) |
| Integrity Check | HMAC-SHA256 |
| Key Space | 2²⁵⁶ |
| External Libraries | None (pure Python stdlib) |

---

## 🌿 Branches

| Branch | Description |
|---|---|
| `main` | v1 — Caesar Cipher (basic, educational) |
| `v2-secure-cipher` | v2 — PBKDF2 + XOR + HMAC (production-level security) |

---

## 👤 Author

**Saurabh**
GitHub: (https://github.com/your-username)
Linkedin: (www.linkedin.com/in/saurabh-p-pandey-754923414)


---

## 📄 License

MIT License — free to use, modify, and distribute.
