# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# first_even(nums) 함수를 정의한다.
def first_even(nums):
    # 순회하여 짝수를 찾으면 그 값 반환
    for x in nums:
        if x % 2 == 0:
            return x
    # 짝수가 하나도 없으면 "None"
    return "None"

# 함수를 호출하여 결과를 출력한다.
print(first_even(nums))