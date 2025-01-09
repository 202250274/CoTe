
word = input()
answer = [-1] * 26
for idx, i in reversed(list(enumerate(word))):
    answer[ord(i)-97] = idx
    
print(*answer)