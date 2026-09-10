# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "3661" 이면 sec == 3661
sec = int(input())

# to_hms 함수를 정의한다.
def to_hms(sec):
    # 시간, 분, 초 값을 반환한다.
    hours = sec // 3600
    minutes = (sec % 3600) // 60
    seconds = sec % 60
    return hours, minutes, seconds

# 언패킹하여 출력한다.
hours, minutes, seconds = to_hms(sec)
print(hours, minutes, seconds)