# values 의 합을 항목 수로 나눠 평균.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 값들의 시퀀스를 반환
values = scores.values()

# 평균
average = sum(values) / len(values)

# 결과 출력
print(f"평균: {average:.1f}")