import sys
lines = sys.stdin.read().splitlines()

tests = lines[1:]
for test in tests:
    H,W,N = map(int,test.split())
    H_1 = str(N%H)
    if H_1 == '0':
        H_1 = str(H)
        W_1 = str(N//H).zfill(2)
    else:
        W_1 = str((N//H) + 1).zfill(2)
    print(int(H_1+W_1))
