# 분모(max - min) 가 0 인 경우는 입력 데이터에서 보장하지 않음 (모든 시나리오 range > 0).
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# 최고값
max_value = max(scores)

# 최솟값
min_value = min(scores)

# 빈 리스트 생성
result = []

# 순회하여 리스트에 저장
for x in scores:
    value = (x - min_value) / (max_value - min_value)
    result.append(value)

# 소수점 둘째 자리까지 출력
print(" ".join(f"{v:.2f}" for v in result))