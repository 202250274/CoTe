n = int(input())
num = 0
for i in range(int(n/1000),n+1):
    n_str = list(str(i))
    if i+int(sum(map(int,n_str))) == n:
        num+=i
        break
print(num)

