# 첫 토큰=기준값(threshold), 나머지=검사할 정수들. 예: "5 3 6 1 8" → threshold=5, nums=[3, 6, 1, 8]
parts = input().split()
threshold = int(parts[0])
nums = [int(x) for x in parts[1:]]

# TODO: 여기에 함수 count_above(threshold, *nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def count_above(threshold, *nums):
    return sum(1 for num in nums if num > threshold)

# ↓ 호출부 (수정하지 마세요) — threshold 는 위치 인자, 나머지는 * 로 풀어 전달
print(count_above(threshold, *nums))