    # 외부 순회 + 내부 dict sum/len 으로 학생별 평균.
data_sets = [
    {
        "윤서": {"수학": 85, "영어": 90, "과학": 78},
        "지우": {"수학": 92, "영어": 88, "과학": 95},
        "민준": {"수학": 65, "영어": 70, "과학": 80},
    },
    {
        "A": {"수학": 90, "영어": 80},
        "B": {"수학": 70, "영어": 80},
    },
    {
        "혼자": {"수학": 80},
    },
]
t = int(input())
students = data_sets[t]

# 순회하여 이름과 과목을 가져옴
for name, subs in students.items():

    # 평균
    avg = sum(subs.values()) / len(subs)
    
    # 결과 출력
    print(f"{name}: {avg:.1f}")