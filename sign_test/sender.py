# [송신자] 자신의 비공개 키로 메시지에 서명한다.
from pathlib import Path
from cryptography.hazmat.primitives.serialization import load_ssh_private_key

# 1. 비공개 키 읽기
key_bytes = Path("test").read_bytes()
private_key = load_ssh_private_key = load_ssh_private_key(key_bytes, password=None)

# 2. 보낼 메시지 입력받기
text = input("보낼 메시지: ")
message = text.encode("utf-8")

# 3. 서명 만들기
signature = private_key.sign(message)
print("서명: ", signature.hex())
