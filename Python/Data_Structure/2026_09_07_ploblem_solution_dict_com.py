# 조건 표현식을 dict comp 값 자리에 두고, zip 으로 짝 지어 순회하세요.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["혼자"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [100, 55, 72],
    [85],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]
# dict 컴프리헨션
grades = {name: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F' 
for name, score in zip(names, scores)}
# 반복하여 key값, value값 출력
for names, scores in grades.items():
    print(f"{names}: {scores}")