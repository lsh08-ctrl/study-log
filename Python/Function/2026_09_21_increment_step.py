# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 증가폭(1), 2개면 둘째 값이 증가폭입니다. (정수)
parts = input().split()


# increment 함수를 정의한다.
def increment(n, step=1):
    # n + step 값 반환
    return n + step

# 입력값이 1개 일 때
if len(parts) == 1 :
    n = int(parts[0])
    print(increment(n))

# 입력값이 2개 일 때
else:
    n = int(parts[0])
    step = int(parts[1])
    print(increment(n, step))