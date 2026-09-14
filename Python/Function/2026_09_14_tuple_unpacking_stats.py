# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# stats(nums) 함수를 정의한다.
def stats(nums):
    total = sum(nums)
    # 최솟값, 최댓값, 합을 반환한다.
    return min(nums), max(nums), total

# 언패킹
min, max, total = stats(nums)

# 함수를 호출하여 결과를 출력
print(min, max, total)