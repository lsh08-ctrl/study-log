# 각 학생마다 scores 를 순회하며 더 높은 점수 개수 + 1.
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

# 순회하여 이름과 점수를 가져옴
for name, score in zip(names, scores):
    
    # 등 수 세기
    count = 0

    for i in scores:
        if i > score:
            count += 1
    
    rank = count + 1

    # 결과 출력
    print(f"{name}: {rank}등")