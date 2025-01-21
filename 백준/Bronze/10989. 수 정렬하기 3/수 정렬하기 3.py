import sys

# 입력 받기
n = int(sys.stdin.readline())
count = [0] * 10001  # 숫자는 10000 이하의 자연수

# 각 숫자의 등장 횟수 세기
for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

# 결과 출력
for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)