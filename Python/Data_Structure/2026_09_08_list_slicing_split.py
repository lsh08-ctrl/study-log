# 두 슬라이스 `data[:k]` 와 `data[k:]` 로 한 번에 분할합니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
p = int(input())
# 분활 위치를 
k = len(data) * p // 100
# k까지의 값
train = data[:k]
# k 다음 값
val = data[k:]
# 결과 출력
print("train:"," ".join(map(str, train)))
print("val:"," ".join(map(str, val)))