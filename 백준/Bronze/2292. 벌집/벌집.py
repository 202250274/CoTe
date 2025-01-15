n = int(input())
a = 1
while n-1>0:
    if n==1:
        break
    n -=(a*6)
    a+=1
print(a)