import sys
lines = sys.stdin.read().splitlines()
N = int(lines[0])
scores = list(map(int, lines[1].split()))
max_scores = max(scores)
avg = 0
for i in scores:
    avg+=(i/max_scores)*100

print(avg/N)