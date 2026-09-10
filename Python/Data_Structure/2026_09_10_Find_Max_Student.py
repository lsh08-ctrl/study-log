# 최댓값 위치를 찾아 이름 리스트에서 같은 인덱스 학생 출력.
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
# 최댓값의 인덱스를 찾는다.
max_index = scores.index(max(scores))

# 최댓값을 가진 학생의 이름 출력
print(names[max_index])