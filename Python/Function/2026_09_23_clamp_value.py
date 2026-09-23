# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 low, high 가 기본값으로 채워집니다. (모두 정수)
parts = input().split()

# clamp 함수를 정의한다.
def clamp(value, low=0,high=100):
    if value < low:
        return int(low)
    elif value > high:
        return int(high)
    else:
        return int(value)


# 입력값이 1개 일 때
if len(parts) == 1:
    print(clamp(int(parts[0])))

# 입력값이 2개일 때
elif len(parts) == 2:
    print(clamp(int(parts[0]), int(parts[1])))

# 입력값이 3개일 때
else:
    print(clamp(int(parts[0]), int(parts[1]), int(parts[2])))