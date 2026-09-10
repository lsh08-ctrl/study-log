    # for문으로 순회하며 '('와 ')'의 개수를 각각 세세요.
s = input()

# 여는 괄호의 개수
open_count = 0
# 닫는 괄호의 개수
close_count = 0

# 문자열 순회
for ch in s:
    if ch == "(":
        # 1씩 누적
        open_count += 1
    elif ch == ")":
        # 1씩 누적
        close_count += 1

# 여는 괄호와 닫는 괄호의 개수가 같으면
# "올바름" 출력 다르면 "올바르지 않음" 출력
if open_count == close_count:
    print("올바름")
else:
    print("올바르지 않음")