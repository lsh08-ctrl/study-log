# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]


# stats4(nums) 함수를 정의한다.
def stats4(nums):
    average = sum(nums) // len(nums)
    # 최솟값, 최댓값, 합, 평균 값을 반환한다.
    return min(nums), max(nums), sum(nums), average

# 언패킹
total = stats4(nums)

# 결과 출력
print(*total)