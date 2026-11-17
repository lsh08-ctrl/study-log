# [송신자] 받는 사람의 공개 키로 메시지를 암호화한다

from pathlib import Path
from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# 1. 받는 사람의 공개 키 읽기
key_bytes = Path("rsa_test.pub").read_bytes()
public_key = load_ssh_public_key(key_bytes)

# 2. 비밀 메시지 입력받기
text = input("보낼 비밀 메시지: ")
message = text.encode("utf-8")

# 3. 공개 키로 암호화
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)
print("암호문:", ciphertext.hex())