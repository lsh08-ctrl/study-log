# 위치: 첫째=기본가, 나머지=품목 금액. "tax=값" 은 키워드 전용 세율(%), 그 외 "key=값" 은 추가 비용(fees, 정수).
raw = input().split()
pos = [t for t in raw if "=" not in t]
base = int(pos[0])
items = [int(x) for x in pos[1:]]
tax = 0
fees = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "tax":
            tax = int(v)
        else:
            fees[k] = int(v)

# invoice 함수를 정의한다.
def invoice(base, *items, tax=0, **fees):
    # 기본가, 품목 금약, 값을 반환한다.
    return (base + sum(items)) + (base * tax // 100) + sum(fees.values())
  
# ↓ 호출부 (수정하지 마세요)
print(invoice(base, *items, tax=tax, **fees))
