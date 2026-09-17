# 정답 37을 맞추는 숫자 야구 게임
answer = "37"
count = 0

while  True: 
    # 숫자를 입력받는다.
    value = input()
    # 입력 횟수 1씩 증가
    count += 1

    # 스트라이크와 볼의 개수
    strike = 0
    ball = 0

    # 2자리 숫자를 하나씩 확인한다.
    for i in range(2):
        if value[i] == answer[i]:
            strike += 1
        elif value[i] in answer:
            ball += 1
    
    # 스트라이크가 2개면 정답
    if strike == 2:
        print(f"정답! {count}번 만에 맞춤")
        break
    # 둘다 0개면 아웃
    elif strike == 0 and ball == 0:
        print("아웃")
    # 그 외에는 스트라이크와 볼을 출력
    else:
        print(f"{strike}스트라이크 {ball}볼")