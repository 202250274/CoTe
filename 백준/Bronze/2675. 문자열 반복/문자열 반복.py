import sys
from itertools import chain, repeat
input = sys.stdin.read().splitlines()
for rep in input[1:]:
    n = int(rep.split()[0])
    s = rep.split()[1]         
    print(''.join(chain.from_iterable(repeat(c,n)for c in s)))
    