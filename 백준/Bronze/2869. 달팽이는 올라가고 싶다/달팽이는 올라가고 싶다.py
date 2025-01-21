A, B, V = map(int,input().split())
day=0
diff = A-B
if (V-A)%diff==0:
    print((V-A)//diff + 1)
else:
    print((V-A)//diff + 2)
