# 콜라츠 추측 과정과 횟수를 출력하세요.
n = int(input())

# 입력받은 횟수를 누적
count = 0

# 1이 될 때 까지 반복
while n != 0:
    print(n)

    if n == 1:
        break
    
    if n % 2 == 0 :
        n = n // 2
    
    else:
        n = (n * 3) + 1
    
    count += 1

# 횟수 출력
print(f"횟수: {count}")