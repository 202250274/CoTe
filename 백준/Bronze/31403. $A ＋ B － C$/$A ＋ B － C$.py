import sys
nums = list(map(int, sys.stdin.read().splitlines()))
print(nums[0]+nums[1]-nums[2])
print(int(str(nums[0])+str(nums[1]))-nums[2])