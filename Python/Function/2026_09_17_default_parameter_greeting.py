# 한 줄을 공백으로 나눕니다. 예: "철수" → ["철수"](기본값 사용) / "철수 반가워" → ["철수","반가워"](override)
parts = input().split()

# TODO: greeting 에 기본값을 가진 함수를 직접 정의(def)하고,
#   토큰 개수(len(parts))에 따라 인자를 생략/전달해 호출한 뒤 결과를 print 하세요.

def greet(name, greeting="안녕하세요"):
    return f"{greeting}, {name}님!"

# 입력값이 한개면 기본 인사말 출력

if len(parts) == 1:
    print(greet(parts[0]))

# 1개가 아니면 인사말을 바꿔 출력
else:
    print(greet(parts[0],parts[1]))