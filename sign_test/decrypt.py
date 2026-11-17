# [수신자] 내 비공개 키로 암호문을 복호화한다

from pathlib import Path
from cryptography.hazmat.primitives.serialization import load_ssh_private_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# 1. 내 비공개 키 읽기
key_bytes = Path("rsa_test").read_bytes()
private_key = load_ssh_private_key(key_bytes, password=None)

# 2. 받은 암호문 입력받기
hex_text = input("받은 암호문(hex): ")
ciphertext = bytes.fromhex(hex_text)

#3. 비공개 키로 복호화
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)
print("복호화된 메시지:", plaintext.decode("utf-8"))