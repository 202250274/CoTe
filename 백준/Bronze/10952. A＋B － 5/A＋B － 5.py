import sys
lines = sys.stdin.read().splitlines()


for i in lines[:-1]:
    print(sum(map(int, i.split())))