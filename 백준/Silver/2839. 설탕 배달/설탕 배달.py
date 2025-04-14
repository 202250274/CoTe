sugar = int(input())
N=-1

max_5 = sugar//5
for i in reversed(range(max_5+1)):
    if sugar % 5 == 0:
        N=max_5
        break
    rest = sugar - (5*i)
    if rest % 3 == 0:
        N = i + rest // 3
        break
    else:
        continue
print(N)  