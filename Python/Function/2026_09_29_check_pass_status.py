# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 커트라인(60), 2개면 둘째 값이 커트라인입니다. (정수)
parts = input().split()

# check_pass 함수를 정의한다. 
def check_pass(score, pass_line=60):
    if score >= pass_line:
        # 값 반환
        return "합격"
    else:
        return "불합격"

# 입력값이 1개 일 때
if len(parts) == 1:
    print(check_pass(int(parts[0])))

# 입력값이 2개 일 때
else:
    print(check_pass(int(parts[0]), (int(parts[1]))))