# key=value 토큰을 dict 로 파싱합니다. 예: "b=2 a=1" → opts={"b":"2","a":"1"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# TODO: 여기에 함수 list_keys(**kwargs) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def list_keys(**kwargs):
    total = sorted(kwargs)
    return ','.join(total)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(list_keys(**opts))
