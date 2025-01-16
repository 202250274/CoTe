import sys

lines = sys.stdin.read().splitlines()
string = str(lines[1])
ha = 0 
for idx, i in enumerate(string):
    ha += (ord(i)-96)*(31**idx)
print(ha%1234567891)