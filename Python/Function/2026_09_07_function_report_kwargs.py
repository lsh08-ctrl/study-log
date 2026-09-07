# 위치 토큰: 첫째=제목, 나머지=정수. "unit=값" 은 키워드 전용 단위.
# 예: "거리 10 20 unit=km" → title="거리", values=[10,20], unit="km"
raw = input().split()

# 1. 위치 인자(pos)와 키워드 인자(kwargs) 분리
pos = [t for t in raw if "=" not in t]
kwargs = dict(t.split("=", 1) for t in raw if "=" in t)

title = pos[0]
values = [int(x) for x in pos[1:]]
unit = kwargs.get("unit", "개")  # unit 키가 없으면 기본값 "개" 사용

# report 함수 정의
def report(title, *values, unit="개"):
    return f"{title}: {sum(values)}{unit}"

# 호출부 (unit은 키워드 전용 전달)
print(report(title, *values, unit=unit))