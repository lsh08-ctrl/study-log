# [수신자] 송신자의 공개 키로 서명을 검증한다.

from pathlib import Path
from cryptography.hazmat.primitives.serialization import load_ssh_public_key
from cryptography.exceptions import InvalidSignature

# 1. 공개 키 읽기
key_bytes = Path("test.pub").read_bytes()
public_key = load_ssh_public_key(key_bytes)

# 2. 받은 메시지와 서명 입력받기
text = input("받은 메시지: ")
message = text.encode("utf-8")

hex_text = input("받은 서명(hex): ")
signature = bytes.fromhex(hex_text)

# 3. 검증하기
try:
    public_key.verify(signature, message)
    print("검증 성공: 송신자가 쓴게 맞고, 내용도 안 바뀌었어요.")
except InvalidSignature:
    print("검증 실패: 위조되었거나 내용이 바뀌었어요.")