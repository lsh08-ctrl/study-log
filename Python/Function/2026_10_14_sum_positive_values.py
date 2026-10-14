# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=5 b=-3" → opts={"a":5,"b":-3}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# TODO: 여기에 함수 sum_positive_values(**kwargs) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def sum_positive_values(**kwargs):
    total = 0
    for x in kwargs.values():
        if x > 0:
            total += x
    return total 

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(sum_positive_values(**opts))
