# max 와 min 의 차이를 직접 출력.
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# 최고값과 최솟값의 차
sub_scores = max(scores) - min(scores)

# 결과 출력
print(sub_scores)