# (점수, 이름) tuple 리스트로 묶어 sort(reverse=True) 후 N-1 인덱스로 접근.
names  = ["윤서", "지우", "민준", "서윤", "도윤"]
scores = [85, 92, 65, 78, 95]
n = int(input())

# tuple 리스트로 묶는다
students = list(zip(scores, names))

# 점수 순으로 정렬
students.sort(reverse=True)

# 언패킹
scores, names = students[n - 1]

# 결과 출력
print(f"{names}: {scores}")