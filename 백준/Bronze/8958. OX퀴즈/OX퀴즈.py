import sys

lines = sys.stdin.read().splitlines()
cases = lines[1:]
for case in cases:
    score=0
    score_li = []
    for i in case:
        if i == 'O':
            score+=1
            score_li.append(score)
        else:
            score=0
            score_li.append(score)
            
    print(sum(score_li))
            
        