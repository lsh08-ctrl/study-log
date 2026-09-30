# `scores.values()` 를 순회하며 cutoff 이상인 값의 개수를 세세요.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# cutoff 이상 학생 수
total = 0

# 순회하여 total에 누적
for name, score in scores.items():
    if score >= cutoff:
        total += 1

# 결과 출력
print(total)
