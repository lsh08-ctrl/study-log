# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 tax, ship 이 기본값으로 채워집니다. (모두 정수)
parts = input().split()

# price_with_opt 함수를 정의한다.
def price_with_opt(base, tax=10, ship=0):

    # 값 반환
    return base + base * tax // 100 + ship

# 토큰이 1개 일 때
if len(parts) == 1:
    print(price_with_opt(int(parts[0])))

# 토큰이 2개 일 때
elif len(parts) == 2:
    print(price_with_opt(int(parts[0]), int(parts[1])))

# 토큰이 3개 일 때
else:
    print(price_with_opt(int(parts[0]), int(parts[1]), int(parts[2])))
