import sys
lines = sys.stdin.read().splitlines()

N, X = map(int, lines[0].split())
nums = list(map(int, lines[1].split()))
smaller = []
for i in nums:
    if i < X:
        smaller.append(i)
print(*smaller)