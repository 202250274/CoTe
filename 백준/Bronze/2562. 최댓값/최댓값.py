import sys
nums = list(map(int, sys.stdin.read().splitlines()))
num=0
for idx, n in enumerate(nums):
    if n > num:
        num = n
        num_idx = idx+1
print(num)
print(num_idx)