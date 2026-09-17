# 평균 변수 한 번 계산 후 두 그룹 list 에 분류.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["X", "Y"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 평균 이상과 평균 미만 리스트 생성
above = []
below = []

# 평균을 구한다.
avg = sum(scores) / len(scores)

# 순회하여 평균이상과 평균 미만을 찾아낸다.
for name, score in zip(names, scores):
    if score >= avg:
        above.append(name)
    else:
        below.append(name)

# 결과 출력
print(f"평균 이상: {' '.join(above)}")
print(f"평균 미만: {' '.join(below)}")