h, m = map(int, input().split())
if m < 45 :
    if h == 0:
        h = 23
        m = 15+m
    else:
        m = 15+m
        h -= 1
else:
    m = m-45
print(h, m)