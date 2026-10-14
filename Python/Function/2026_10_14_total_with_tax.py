# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "price=1000 tax=10" → opts={"price":1000,"tax":10}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# TODO: 여기에 함수 total_with_tax(price, tax) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def total_with_tax(price, tax):
    return price + price * tax // 100

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(total_with_tax(**opts))
