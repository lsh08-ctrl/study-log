# 두 dict 각각의 `in` 으로 분기. 부호 표시는 f-string의 `{diff:+d}` 가 깔끔합니다.
s1 = {"윤서": 85, "지우": 92, "민준": 65}
s2 = {"지우": 88, "민준": 70, "도윤": 95}
name = input()

# 양 학기 모두 있으면
if name in s1 and name in s2:
    # 차이
    diff = s2[name] - s1[name]
    # 변화 출력
    print(f"변화: {diff:+d}")

# 한 학기만 있으면
elif name in s1 or name in s2:
    print("한 학기만")

# 양 학기 모두 있으면
else:
    print("없음")