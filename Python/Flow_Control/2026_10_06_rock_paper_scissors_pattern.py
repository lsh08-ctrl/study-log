# 컴퓨터 패턴과 비교하여 승패를 판정하세요.
n = int(input())

# 승, 무, 패를 저장할 변수
win = 0
lose = 0
draw = 0

# 3번 반복
for i in range(n):
    
    # 플레이어의 선택을 입력받는다.
    player = input()
    
    if i % 3 == 0:
        computer = "바위"
    
    elif i % 3 == 1:
        computer = "보"
    
    else:
        computer = "가위"
    
    # 승리하였을 때
    if (player == "가위" and computer == "보") or \
       (player == "보" and computer == "바위") or \
       (player == "바위" and computer == "가위"):
       result = "승"
       win += 1
    
    # 비겼을 때
    elif player == computer:
        result = "무"
        draw += 1
    
    # 졌을 때
    else:
        result = "패"
        lose += 1
    
    print(f"{i + 1}판: 플레이어({player}) vs 컴퓨터({computer}) -> {result}")

# 총 결과 출력
print(f"전적: {win}승 {lose}패 {draw}무")