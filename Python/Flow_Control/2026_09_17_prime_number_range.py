# 구간 내 소수를 찾아 출력하세요.
start = int(input())
end = int(input())

for n in range(start, end + 1):
    if n < 2:
        continue
    
    # n의 약수 개수를 확인
    count = 0

    for i in range(1, + n + 1):
        if n % i == 0:
            count += 1
     # 약수가 2개인 수가 소수
    if count == 2:
        print(n, end=' ')