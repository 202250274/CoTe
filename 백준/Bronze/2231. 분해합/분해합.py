n = int(input())
num = 0
for i in range(int(n/1000),n+1):
    if i+sum(map(int,str(i))) == n:
        num+=i
        break
print(num)

