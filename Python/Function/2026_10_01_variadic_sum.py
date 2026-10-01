# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 함수 total(*nums) 를 직접 정의(def)한다. 
def total(*nums):
    total = 0
    for num in nums:
        total += num
    return total
# 리스트를 * 로 풀어 total 에 전달
print(total(*nums))