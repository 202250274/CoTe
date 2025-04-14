import sys
lines = sys.stdin.read().splitlines()
N, M = map(int, lines[0].split())
l = [list(line) for line in lines[1:]]
min_changes = 50*50

for start_row in range(N-7):
    for start_col in range(M-7):
        count_w = 0
        count_b = 0
        
        for i in range(8):
            for j in range(8):
                current = l[start_row+i][start_col + j]
                
                if (i+j) % 2 ==0:
                    if current != 'W':
                        count_w+=1
                    if current !='B':
                        count_b += 1
                else:
                    if current !='B':
                        count_w+=1
                    if current !='W':
                        count_b += 1
        min_changes = min(min_changes, count_w, count_b)
                        

print(min_changes)