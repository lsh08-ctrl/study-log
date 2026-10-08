# 발견 여부를 추적하는 플래그 변수를 사용합니다. 조건을 만족하는 첫 원소에서 break.
nums = [4, 7, 15, 3, 22, 9]

# k를 입력받는다.
k = int(input())

# 플래그 변수
found = False

# 순회하여 원소와 인덱스를 가져옴
for i, j in enumerate(nums):
    # k 이상인 원소를 찾으면
    if j >= k:
        # 위치, 값 출력
        print(f"위치: {i}")
        print(f"값: {j}")
        found = True
        break

# 끝까지 찾지 못하면
if not found:
    print("찾지 못했습니다")