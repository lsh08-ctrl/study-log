# 첫 토큰=개수(k), 나머지=정수들. 예: "2 1 2 3 4" → k=2, nums=[1, 2, 3, 4]
parts = input().split()
k = int(parts[0])
nums = [int(x) for x in parts[1:]]

# TODO: 여기에 함수 top_k_sum(k, *nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def top_k_sum(k, *nums):
    return sum(sorted(nums, reverse=True)[:k])

# ↓ 호출부 (수정하지 마세요) — k 는 위치 인자, 나머지는 * 로 풀어 전달
print(top_k_sum(k, *nums))
