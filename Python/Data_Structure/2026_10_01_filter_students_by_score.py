# `for name, s in scores.items():` 순회하며 조건 만족하는 이름을 모으세요.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# 컴프리헨션으로 저장
result = [name for name, s in scores.items() if s >= cutoff]

# 결과 출력
print(*result)