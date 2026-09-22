# 동률 시 갱신 안 하도록 strict less (<) 사용.
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

# 평균값
average = sum(scores) / len(scores)

# 평균에 가장 가까운 점수
best_score = scores[0]
# 평균에 가장 가까운 학생
best_name = names[0]
# 가장 큰 차
best_diff = abs(scores[0] - average)

# 순회하여 이름과 점수를 가져옴
for name, score in zip(names, scores):
    diff = abs(score - average)
    
    if diff < best_diff:
        best_diff = diff
        best_name = name
        best_score = score

# 결과 출력
print(f"{best_name}: {best_score}")