import sys
lines = sys.stdin.read().splitlines()
nums = list(map(int, lines[1].split()))
sosu = 0
for num in nums:
    if num ==1:
        continue
    for i in range(2,num+1):
        if i == num :
            sosu+=1
            break
        elif num%i == 0:
            break

print(sosu)