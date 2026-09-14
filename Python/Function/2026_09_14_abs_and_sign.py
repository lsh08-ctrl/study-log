# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "-5" 이면 n == -5
n = int(input())

# TODO: 절댓값과 부호 문자열을 함께 return 하는 함수를 직접 정의(def)하고,
#   반환값을 언패킹해 "절댓값 부호" 형식으로 출력(print)하세요.
def abs_sign(n):
    if n < 0:
        return -n, "음수"
    elif n == 0:
        return n, 0
    else:
        return  n, "양수"
abs_value, sign = abs_sign(n)
print(abs_value, sign)