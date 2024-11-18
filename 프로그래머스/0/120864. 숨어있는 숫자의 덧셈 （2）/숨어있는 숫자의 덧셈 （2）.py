def solution(my_string):
    import re
    nums = re.findall(r'\d+', my_string)
    answer = sum(map(int, nums))

    return answer