# 각 감가율을 따로 계산한 뒤 합산하고 최저가를 체크하세요.
new_price = int(input())
year = int(input())
km = float(input())
accident = input()
# 연식 감가율
if year <= 3:
    year_discount = year * 10
elif year <= 7:
    year_discount = 3 * 10 + (year - 3) * 7
else:
    year_discount = 3 * 10 + 4 * 7 + (year - 7) * 5
# 주행거리 감가율
if km <= 5:
    km_discount = 0
elif km <= 10:
    km_discount = 5
else:
    km_discount = 10
# 사고 감가율
if accident == "Y" or  accident == "y":
    accident_discount = 15
else:
    accident_discount = 0
# 총 감가율
total_discount = year_discount + km_discount + accident_discount
# 최종 가격
last_price = int(new_price * (1 - total_discount / 100))
# 최소 가격
min_price = int(new_price * 0.1)
if last_price < min_price: # 최종가격이 최소가격보다 작을 시
    last_price = min_price  # 최종가격 = 최소가격

# 출력
print("--- 감가 내역 ---")
print(f"연식 감가 ({year}년): {year_discount}%")
print(f"주행거리 감가: {km_discount}%")
print(f"사고 감가: {accident_discount}%")
print(f"총 감가율: {total_discount}%")
print(f"예상 중고차 가격: {last_price}만원")