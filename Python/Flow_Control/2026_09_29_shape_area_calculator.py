# 도형 종류에 따라 필요한 값을 입력받으세요.
shape = input()

# 입력값이 원 일 때
if shape == "원":
    r = int(input())
    result = r * r * 3.14
    print(f"넓이: {result:.2f}")

# 입력값이 삼각형 일 때
elif shape == "삼각형":
    # 밑변
    base = int(input())
    # 높이
    height = int(input())
    result = base * (height / 2)
    print(f"넓이: {result:.1f}")

# 입력값이 사각형 일 때
elif shape == "사각형":
    # 가로
    width = int(input())
    # 세로
    height = int(input())
    result = width * height
    print(f"넓이: {result}")