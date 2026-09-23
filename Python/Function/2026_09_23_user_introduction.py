# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 age, city 가 기본값으로 채워집니다. (age 는 정수)
parts = input().split()


# 함수 introduce를 정의한다.
def introduce(name, age=20, city="서울"):
    # 이름, 나이, 도시 값을 반환
    return f"{name}/{age}/{city}"

# 입력값이 1개이면 나이, 도시는 기본값
if len(parts) == 1:
    print(introduce(parts[0]))

# 입력값이 2개이면 도시만 기본값
elif len(parts) == 2:
    print(introduce(parts[0],parts[1]))

# 입력값이 3개이면 모두 지정한다.
else:
    print(introduce(parts[0], parts[1], parts[2]))