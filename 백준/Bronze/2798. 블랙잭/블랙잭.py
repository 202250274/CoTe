import sys
from itertools import combinations

lines = sys.stdin.read().splitlines()
N, M = map(int, lines[0].split())
cards = list(map(int,lines[1].split()))
cards_max = 0
for i in combinations(cards, 3):
    cards_sum = sum(i)
    if cards_sum <= M:
        cards_max = max(cards_sum, cards_max)
        
print(cards_max)




