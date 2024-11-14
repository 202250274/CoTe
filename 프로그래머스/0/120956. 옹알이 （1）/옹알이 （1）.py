def solution(babbling):
    canbab = ['aya', 'ye', 'woo', 'ma']
    n=0
    for bab in babbling:
        for i in canbab:
            if i in bab:
                bab = bab.replace(i,' ')
                if bab.isspace():
                    n+=1
                    break
    answer = n
    return answer