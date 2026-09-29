# 각 누적 슬라이스의 평균을 모아 한 줄로 출력.
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# 평균 값을 담을 리스트 생성
averages = []

# 순회하여 인덱스와 값을 가져옴
for i, score in enumerate(scores):
     
    # 슬라이스
    slice = scores[:i+1]
    
    # 평군
    average = sum(slice) / len(slice)

    # 리스트에 누적
    averages.append(average)

# 결과 출력
print(" ".join(f"{v:.1f}" for v in averages))