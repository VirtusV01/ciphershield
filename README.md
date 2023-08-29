# GUI Based Encryption and Decryption Application

This is a simple graphical user interface (GUI) application written in Python using the Tkinter library to perform RSA encryption and decryption. The application allows you to encrypt a message using RSA public key and decrypt an encrypted message using the corresponding RSA private key.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Basic file encryption and decryption using a generated key.
- Password-based file encryption and decryption with salted key derivation.
- Seamless integration with the `cryptography` library.
- Clear and organized functions for common encryption tasks.

## Installation

1. Clone the repository:

```shell
   git clone https://github.com/VirtusV01/CipherShield.git

```
   
2. Navigate to the project directory:

```shell
   cd CipherShield

```
   
3. Install the required dependencies:

```shell
   pip install cryptography

```
4. Execute:

```shell
   python ciphershield.py

```

## Usage

The CipherShield library provides several functions for encryption and decryption tasks. You can use these functions in your own Python scripts or as part of your projects.

## Basic Encryption

```shell
from crypto.crypto import basic_encryption

key = basic_encryption('path/to/your/file.txt')
print("Encryption key:", key)

```
## Basic Decryption

```shell
from crypto.crypto import basic_decryption

plaintext = basic_decryption('path/to/your/crypted_file.txt')
print("Decrypted content:", plaintext.decode('utf-8'))

```
## Encryption with Password

```shell
from crypto.crypto import encryption_with_psw

encryption_with_psw('path/to/your/file.txt', 'your_password')

```

## Decryption with Password

```shell
from crypto.crypto import decryption_with_psw

plaintext = decryption_with_psw('path/to/your/crypted_file.txt', 'your_password')
print("Decrypted content:", plaintext.decode('utf-8'))

```


## Contributing

Contributions are welcome! If you'd like to contribute to PyEncryptor, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: git checkout -b feature-name
3. Make your changes and add appropriate tests.
4. Commit your changes: git commit -am 'Add new feature'
5. Push to the branch: git push origin feature-name
6. Submit a pull request.

## License

MIT License

<p align="justify">Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>


