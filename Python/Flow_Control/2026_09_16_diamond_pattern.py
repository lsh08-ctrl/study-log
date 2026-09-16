# 홀수 N을 입력받아 마름모를 출력하세요.
n = int(input())
# 순회하여 마름모 출력
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)

for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)