def solution(my_string, num1, num2):
    my_str1 = my_string[num1]
    my_str2 = my_string[num2]
    answer = my_string[:num1]+my_str2+my_string[num1+1:num2]+my_str1+my_string[num2+1:]

    return answer