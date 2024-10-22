def solution(s):
    num2en = {
        'zero':'0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    
    answer = ''
    temp = ''
    for i in s:    
        temp += i
        if temp in num2en:
            answer += num2en[temp]
            temp = ''
        elif temp in num_list:
            answer += temp
            temp = ''
    return int(answer)