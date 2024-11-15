def solution(quiz):
    answer = []
    for i in quiz:
        split_i = i.split(' ')
        if split_i[1] == '+':
            if int(split_i[0]) + int(split_i[2]) == int(split_i[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(split_i[0]) - int(split_i[2]) == int(split_i[4]):
                answer.append('O')
            else:
                answer.append('X')
            
        
    
    return answer