# 3번 반복하며 계산 결과를 누적하세요.
total = 0

# 3번 반복
for i in range(3):
    # 입력을 받는다. 
    n1, op, n2 = input().split()

    # 정수로 변환
    n1 = int(n1)
    n2 = int(n2)
    
    # 입력값이 + 일 때
    if op == "+":
        result = n1 + n2
    
    # 입력값이 - 일 때
    elif op == "-":
        result = n1 - n2
    
    # 입력값이 * 일 때
    elif op == "*":
        result = n1 * n2
    
    # 입력값이 / 일 떄
    else:
        result = n1 // n2
    
    print(result)
    total += result

# 합계 출력
print(f"합계: {total}")