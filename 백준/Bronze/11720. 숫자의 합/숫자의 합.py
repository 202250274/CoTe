import sys
lines = sys.stdin.read().splitlines()
T = lines[0]


print(sum(map(int, list(lines[1]))))