# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 할인율(10), 2개면 둘째 값이 할인율(%)입니다. (정수)
parts = input().split()

# discount_price 함수를 정의한다.
def discount_price(price, rate=10):
    # 할인률 반환
    return price - price * rate // 100

# 입력값이 1개 일 때
if len(parts) == 1:
    print(discount_price(int(parts[0])))

# 입력값이 2개 일 때
else:
    print(discount_price(int(parts[0]), int(parts[1])))