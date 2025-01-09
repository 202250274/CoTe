import sys
lines = sys.stdin.read().splitlines()
T = lines[0]
nums = list(map(int, lines[1].split()))

print(min(nums),max(nums))