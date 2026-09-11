score = int(input())

def evaluate(score):
    # 범위 밖이면 즉시 반환
    if score < 0 or score > 100:
        return "유효하지 않음"

    # 유효 범위 내에서 합격/불합격 판정
    if score >= 60:
        return "합격"
    return "불합격"

# 결과 출력
print(evaluate(score))