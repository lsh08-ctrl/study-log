# 누적합 변수와 발견 플래그를 둡니다.
# 한 원소를 살필 때 0이면 즉시 continue, 그 외에는 누적합에 더한 직후 K 도달 여부를 검사하세요.
# 반복문 종료 후 플래그로 "한계 미달" 여부를 판정합니다.
nums = [4, 0, 3, 0, 0, 7, 2, 0, 8, 1]
k = int(input())

# 플래그 변수
found = False

# 누적합 변수
total = 0

# 순회하여 인덱스와 숫자를 가져옴
for i, v in enumerate(nums):
    # 원소가 0이면 무시
    if v == 0:
        print(f"무시한 위치: {i}")
        continue
    total += v
    # k 이상이면 종료 누적합 출력
    if total >= k:
        print(f"종료 위치: {i}")
        print(f"최종 누적합: {total}")
        found = True
        break

# # 끝까지 못 넘으면 한계미달, 누적합 출력
if not found:
    print(f"한계 미달, 누적합: {total}")