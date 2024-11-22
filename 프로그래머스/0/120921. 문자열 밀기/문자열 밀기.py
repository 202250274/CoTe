def solution(A, B):
    A_list = list(A)
    A_list_new = A_list
    num_A = len(A_list)
    n=0
    A_new=A
    while A_new!=B:
        A_list = A_list_new.copy()
        for i in range(num_A):
            if i==num_A-1:
                A_list_new[0]=A_list[-1]
            else:
                A_list_new[i+1] = A_list[i]


        n+=1
        A_new = ''.join(A_list_new)
        print(A_new)
        if n==num_A:
            n=-1
            break
    
    answer = n
    return answer