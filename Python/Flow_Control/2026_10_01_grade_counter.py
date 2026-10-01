# 등급별 카운터 4개를 0으로 초기화하고, 입력 0을 종료 조건으로 반복 처리하세요.
count_a = 0
count_b = 0
count_c = 0
count_f = 0
score = int(input())

# 0을 입력받을 때 까지 반복
while score != 0:
    
    # 0 미만
    if score < 0:
        print("잘못된 점수")
    
    # 100 초과
    elif score > 100:
        print("점수 초과")
    
    # 90 이상
    elif 100 >= score >= 90:
        count_a += 1
    # 80 이상
    elif score >= 80:
        count_b += 1
    
    # 70 이상
    elif score >= 70:
        count_c += 1
    
    # 1 이상 69 이하
    else:
        count_f += 1
    
    score = int(input())
# 결과 출력
print(f"A: {count_a} B: {count_b} C: {count_c} F: {count_f}")