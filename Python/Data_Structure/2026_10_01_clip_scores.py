# `min(점수 + n, 100)` 으로 한 번에 clip 할 수 있습니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
n = int(input())

# value값과 키 값을 순회하여 가져옴
for name, s in scores.items():
    # 보너스 저장
    result = min(s + n, 100)
    
    # 결과 출력
    print(f"{name}: {result}")