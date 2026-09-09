# 위치: 첫째=상품, 둘째=가격, 나머지=옵션. "discount=값" 은 키워드 전용, 그 외 "key=value" 는 기타 정보(info).
# 예: "노트북 1000 마우스 키보드 discount=100 color=검정" → product=노트북, price=1000, options=[마우스,키보드], discount=100, info={color:검정}
raw = input().split()
pos = [t for t in raw if "=" not in t]
product = pos[0]
price = int(pos[1])
options = pos[2:]
discount = 0
info = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "discount":
            discount = int(v)
        else:
            info[k] = v

# TODO: 여기에 함수 order2(product, price, *options, discount=0, **info) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
# order2 함수를 정의한다.
def order2(product, price, *options, discount=0, **info):

    # 컴프리헨션으로 키 값과 value 값을 얻는다.
    print_info = [k + "=" + v for k, v in info.items()]
    
    # 상품, 가격, 옵션, 값을 반환한다.
    return f"{product} {price-discount}원 옵션{len(options)}개 [{','.join(sorted(print_info))}]"

# ↓ 호출부 (수정하지 마세요)
print(order2(product, price, *options, discount=discount, **info))