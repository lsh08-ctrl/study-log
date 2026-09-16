# 5개 카운터 + if/elif 분기로 분류.
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# 등급별 카운트를 생성
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0

# 순회하여 점수를 찾음
for s in scores:
    if s >= 90:
        count_a += 1
    
    elif s >= 80:
        count_b += 1
    elif s >= 70:
        count_c += 1
    elif s >= 60:
        count_d += 1
    else:
        count_f += 1
# 각 등급별로 카운트 출력
print(f"A: {count_a}")
print(f"B: {count_b}")
print(f"C: {count_c}")
print(f"D: {count_d}")
print(f"F: {count_f}")