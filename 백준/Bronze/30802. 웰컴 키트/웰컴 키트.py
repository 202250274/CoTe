import sys
lines = sys.stdin.read().splitlines()
N = int(lines[0])
sizes = list(map(int, lines[1].split()))
T, P = map(int, lines[2].split())

shirt_num = 0
for size in sizes:
    num = size//T
    if size % T == 0:
        shirt_num += num
    else:
        shirt_num += num+1
print(shirt_num)
print(N//P, N%P)