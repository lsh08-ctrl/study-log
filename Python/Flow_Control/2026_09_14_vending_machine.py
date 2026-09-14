# while + if/elif + break/continue를 사용하세요.
money = int(input())
# 참 일때만 반복
while money >= 500:
    print(f"잔액: {money}원")
    print("1. 물 (500원)")
    print("2. 주스 (1000원)")
    print("3. 커피 (1500원)")
    
    # 메뉴를 입력받는다.
    menu = int(input())
    # 메뉴에 따른 가격, 종류
    if menu == 1:
        price = 500
        name = "물"
    elif menu == 2:
        price = 1000
        name = "주스"
    elif menu == 3:
        price = 1500
        name = "커피"
    else:
        print("잘못된 선택입니다.")
        continue
    if money >= price:
        money -= price
        print(f"{name}를 선택했습니다.")
    else:
        print("잔액이 부족합니다.")
        break
# 출력
print(f"남은 금액: {money}원")