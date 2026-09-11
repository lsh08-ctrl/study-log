# for + if char != remove: result += char
text = input()
remove = input()
result = ""
# 문자열 길이 만큼 반복
for char in range(len(text)):
    # 아니라면
    if text[char] != remove:
        # 누적
        result += text[char]
# 출력
print(f"결과: {result}")