def solution(my_string):
    split_str = my_string.split(' ')
    
    answer=int(split_str[0])
    for i in range(1,len(split_str),2):
        if split_str[i] == '+':
            answer+=int(split_str[i+1])
        else:
            answer-=int(split_str[i+1])

    return answer