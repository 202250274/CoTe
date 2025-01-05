from collections import Counter
import sys

nums = list(map(int,sys.stdin.read().splitlines()))
ABC = str(nums[0]*nums[1]*nums[2])
dic = Counter(list(ABC))

for i in range(10):
    print(dic[str(i)])
    

