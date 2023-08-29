from crypto.crypto import encrypt_file, decrypt_file
from crypto.crypto import generate_key, generate_filekey, \
                          generate_saltfile, generate_key_from_psw

from pathlib import Path
from shutil import copyfile


def get_path(filepath: Path) -> str:
    """Returns the directory path of a file."""
    return str(filepath.parent)


def read_file(filepath: Path) -> bytes:
    """Reads a file."""
    with open(filepath, 'rb') as f:
        content = f.read()

    return content


def basic_encryption(filepath: str, overwrite=False) -> bytes:
    """Encrypts a file using a generated key, writes the key in the
    same folder as the file, and then returns the key."""
    filepath = Path(filepath)
    path = get_path(filepath)
    key = generate_filekey(path)

    if overwrite:
        encrypt_file(key, filepath)
    else:
        new_filepath = filepath.with_name(f"{filepath.stem}_crypted{filepath.suffix}")
        copyfile(filepath, new_filepath)
        encrypt_file(key, new_filepath)

    return key


def basic_decryption(filepath: str, readonly=False) -> bytes:
    """Decrypts a file using the generated filekey."""
    filepath = Path(filepath)
    path = get_path(filepath)

    key = read_file(Path(path) / 'filekey.key')

    return decrypt_file(key, filepath, readonly)


def encryption_with_psw(filepath: str, psw: str, overwrite=False) -> None:
    """Encrypts a file using a given password, storing the salt in a
    separate file to replicate the key."""
    filepath = Path(filepath)
    path = get_path(filepath)
    psw = psw.encode('utf-8')

    key = generate_key_from_psw(
        psw,
        generate_saltfile(path)
    )

    if overwrite:
        encrypt_file(key, filepath)
    else:
        new_filepath = filepath.with_name(f"{filepath.stem}_crypted{filepath.suffix}")
        copyfile(filepath, new_filepath)
        encrypt_file(key, new_filepath)


def decryption_with_psw(filepath: str, psw: str, readonly=False) -> bytes:
    """Decrypts a file using a given password."""
    path = get_path(Path(filepath))
    psw = psw.encode('utf-8')

    key = generate_key_from_psw(
        psw,
        read_file(Path(path) / 'salt.key')
    )

    return decrypt_file(key, filepath, readonly)
