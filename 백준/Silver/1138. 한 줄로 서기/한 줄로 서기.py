from itertools import permutations
n = int(input())
people = list(map(int, input().split()))
for i in permutations(range(1, n+1), n):
    i = list(i)
    answer = i.copy()
    success = True
    for j in range(1, n):
        idx = i.index(j)
        if len(i[:idx]) == people[j-1]:
            i.remove(j)
        else:
            success = False
            break
    if success:
        print(*answer)
        break