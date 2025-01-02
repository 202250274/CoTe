import sys
input = sys.stdin.read().splitlines()
nums = list(map(int,input))
a_set = set()
for num in nums:
    a = num%42
    a_set.add(a)
print(len(a_set))
    