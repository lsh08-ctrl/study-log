# build_tag 함수를 먼저 정의합니다. (함수 정의는 실행 코드보다 위에 두는 것이 관례)
def build_tag(name, level=1):
    # "#" * level 개 + name 을 반환
    return "#" * level + name  # 연산자 주변 공백을 일관되게 정리


# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 레벨(1), 2개면 둘째 값(정수)이 레벨입니다.
parts = input().split()

# 입력값이 1개 일 때
if len(parts) == 1:
    print(build_tag(parts[0]))

# 입력값이 2개 일 때
else:
    print(build_tag(parts[0], int(parts[1])))