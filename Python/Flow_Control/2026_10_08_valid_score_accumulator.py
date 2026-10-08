# N번 반복하며 점수를 입력받습니다. 범위를 벗어나면 안내 출력 후 continue, 유효한 점수만 누적합에 더하세요.
# 반복문 종료 후 최종 합계를 한 줄 출력합니다.
n = int(input())

# 누적합
total = 0

# 순회하여 반복
for i in range(n):
    
    # 정수를 입력받는다.
    score = int(input())

    # 0 미만 100 초과일 시 -> 무효
    if score < 0 or score > 100:
        print(f"무효: {score}")
        continue

    total += score

# 유효 점수의 합 출력
print(f"유효 점수의 합: {total}")