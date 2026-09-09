# 슬라이싱의 step 인자를 K로 지정하면 균일한 간격으로 추출됩니다.
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
k = int(input())
# k 만큼 스텝하여 슬라이싱한다
step_k_index = data[::k]
# 결과 출력
print(" ".join(map(str, step_k_index)))