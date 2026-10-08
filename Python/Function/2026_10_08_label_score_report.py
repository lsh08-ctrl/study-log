# 첫 토큰=라벨(label), 나머지=점수들. 예: "수학 90 80 70" → label="수학", scores=[90, 80, 70]
parts = input().split()
label = parts[0]
scores = [int(x) for x in parts[1:]]

# TODO: 여기에 함수 report(label, *scores) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def report(label, *scores):
    return f"{label}: {sum(scores)}"

# ↓ 호출부 (수정하지 마세요) — label 은 위치 인자, 나머지는 * 로 풀어 전달
print(report(label, *scores))
