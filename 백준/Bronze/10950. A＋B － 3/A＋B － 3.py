import sys
lines = sys.stdin.read().splitlines()
T = lines[0]

for i in lines[1:]:
    print(sum(map(int, i.split())))