# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# TODO: 여기에 함수 product_all(*nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def product_all(*nums):
    result = 1
    for num in nums:
        result *= num
    return  result

# ↓ 호출부 (수정하지 마세요)
print(product_all(*nums))