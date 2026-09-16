# 첫 줄은 한계값 T, 둘째 줄은 공백으로 구분된 정수들입니다.
# 예: 첫 줄 "10", 둘째 줄 "3 4 5 6" → threshold=10, nums=[3, 4, 5, 6]
threshold = int(input())
nums = [int(x) for x in input().split()]

# first_exceed(nums, threshold) 함수를 정의한다.
def first_exceed(nums, threshold):
    # 누적합 변수
    total = 0
    
    # 순회하여 누적합을 넘는 인덱스를 찾아냄
    for i in range(len(nums)):
        total += nums[i]

        if total > threshold:
        # 누적합을 넘으면 i 반환
            return  i
    # 끝까지 안 넘으면 -1 반환
    return -1

# 함수를 호출하여 출력한다.
print(first_exceed(nums, threshold))