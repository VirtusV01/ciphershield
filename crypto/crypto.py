import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def encrypt_file(key: bytes, filepath: str) -> None:
    """Encrypts a file."""
    fernet = Fernet(key)

    with open(filepath, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(key: bytes, filepath: str, readonly=False) -> bytes:
    """Decrypts a file."""
    fernet = Fernet(key)

    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    if not readonly:
        with open(filepath, 'wb') as dec_file:
            dec_file.write(decrypted)

    return decrypted

def generate_key() -> bytes:
    """Generate a cryptographic key."""
    return Fernet.generate_key()

def generate_filekey(path: str) -> bytes:
    """Generates a file key in the specified path; returns the key."""
    key = generate_key()

    with open(os.path.join(path, 'filekey.key'), 'wb') as filekey:
        filekey.write(key)

    return key

def generate_saltfile(path: str) -> bytes:
    """Generates and stores salt in the salt.key file. Returns the salt."""
    salt = os.urandom(16)

    with open(os.path.join(path, 'salt.key'), 'wb') as saltfile:
        saltfile.write(salt)

    return salt

def generate_key_from_psw(psw: bytes, salt: bytes) -> bytes:
    """Generate a cryptographic key from a password and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=32_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(psw))
    
    return key

if __name__ == "__main__":
    # Example usage
    key = generate_key()
    salt = generate_saltfile('.')
    key_from_psw = generate_key_from_psw(b'password', salt)

    file_path = 'example.txt'
    encrypt_file(key, file_path)
    decrypted_data = decrypt_file(key, file_path)
    print(decrypted_data.decode('utf-8'))
