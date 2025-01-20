import sys
lines = sys.stdin.read().splitlines()

case = int(lines[0])
ks = [int(i) for i in lines[1::2]]
ns = [int(i) for i in lines[2::2]]

for k, n in zip(ks, ns):
    p_1 = [[i for i in range(1, n+1)]]
    for i in range(1, k+1):
        p_1.append([sum(p_1[i-1][:j+1]) for j in range(n)])

    print(p_1[-1][-1])