# 한 줄을 공백으로 나눕니다. 첫 토큰=n, 둘째 토큰(있으면)=start. 토큰 1개면 start 는 기본값 1. (정수)
parts = input().split()

# ragne_sum 함수를 정의한다.
def  range_sum(n, start=1):
    total = 0
    for i in range(start, n + 1):
        total += i
    # total 값 반환
    return total

# 입력값이 1개 일 때
if len(parts) == 1:
    n = int(parts[0])
    print(range_sum(n))

# 입력값이 2개일 때
else:
    n = int(parts[0])
    start = int(parts[1])
    print(range_sum(n, start))
