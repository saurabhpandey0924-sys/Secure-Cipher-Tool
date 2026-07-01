from core.encrypt import encrypt_message
from core.decrypt import decrypt_message


def main():
    print("=" * 50)
    print("   Saurabh - Secure Cipher Tool")
    print("=" * 50)

    while True:
        print("\n1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. About Security")
        print("4. Exit")
        choice = input("\nChoose (1-4): ").strip()

        if choice == "1":
            text = input("\nEnter message to encrypt: ")
            if not text.strip():
                print("❌ Message empty hai.")
                continue
            password = input("Enter password/key: ")
            if not password:
                print("❌ Password empty nahi ho sakta.")
                continue
            result = encrypt_message(text, password)
            print(f"\nEncrypted : {result}")

        elif choice == "2":
            enc = input("\nEnter encrypted message: ").strip()
            if not enc:
                print("❌ Encrypted text daalo pehle.")
                continue
            password = input("Enter password/key: ")
            try:
                result = decrypt_message(enc, password)
                print(f"\nDecrypted : {result}")
            except ValueError as e:
                print(f"\n❌ {e}")

        elif choice == "3":
            print("\n" + "=" * 50)
            print("  Security Info")
            print("=" * 50)
            print("  Algorithm   : XOR with PBKDF2-HMAC-SHA256 key")
            print("  KDF Rounds  : 100,000 iterations")
            print("  Salt        : 16 bytes random (per encryption)")
            print("  HMAC        : SHA-256 integrity check")
            print("  Key Space   : 2^256 (impossible to brute force)")
            print("=" * 50)

        elif choice == "4":
            print("\nExiting...")
            break

        else:
            print("\n❌ Invalid choice.")


if __name__ == "__main__":
    main()