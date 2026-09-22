# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 수량(1), 2개면 둘째 값이 수량입니다. (정수)
parts = input().split()


# total_price 함수를 정의한다.
def total_price(unit_price, count=1):
    # unit_price * count 값을 반환
    return unit_price * count

# 입력값이 1개일 때
if len(parts) == 1:
    print(*total_price(parts))

# 입력값이 2개일 때
else:
    print(total_price(int(parts[0]), int(parts[1])))