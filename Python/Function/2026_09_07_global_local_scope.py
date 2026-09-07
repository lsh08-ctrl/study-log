# 전역 language = 첫 단어, chosen = 둘째 단어. 예: "한국어 영어" → language="한국어", chosen="영어"
parts = input().split()
language = parts[0]
chosen = parts[1]

# setting() (지역 language 사용) 정의
def setting():
    language = chosen  # 지역 변수 선언
    return f"현재: {language}"

# reading() (전역 language 읽기) 정의
def reading():
    return f"기본: {language}"

# setting(), reading(), 전역 language 출력
print(setting())
print(reading())
print(language)