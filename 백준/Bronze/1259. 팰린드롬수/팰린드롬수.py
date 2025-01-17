import sys
lines = sys.stdin.read().splitlines()
a=0
for line in lines[:-1]:
    a=1
    for i in range(len(line)//2):
        if line[i] != line[-(i+1)]:
            print('no')
            a=0
            break
        a=1
    if a==1:
        print('yes')
        a=0
            