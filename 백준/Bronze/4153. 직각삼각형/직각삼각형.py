import sys
lines = sys.stdin.read().splitlines()

for i in lines[:-1]:
    x,y,z = sorted(map(int,i.split()))
    if x**2+y**2==z**2:
        print("right")
    else:
        print("wrong")