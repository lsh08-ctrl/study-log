# 학생 수 입력
n = int(input())

# 10점 구간별 인원수를 저장할 리스트
count = [0] * 10

# 학생 수만큼 점수 입력
for i in range(n):
    score = int(input())

    if score == 100:
        count[9] += 1
    else:
        index = score // 10
        count[index] += 1

for i in range(10):
    if count[i] > 0:

        # 구간의 시작 점수 계산    
        start = i * 10

        # 마지막 구간은 90~100으로 출력
        if i == 9:
            print(f"{start}~100: {'#' * count[i]}")

        # 나머지 구간은 시작 점수~끝 점수로 출력
        else:
            print(f"{start}~{start + 9}: {'#' * count[i]}")