def solution(s):
    s_list = s.split(' ')
    result = []
    for i in s_list:
        if i:
            result.append(i[0].upper() + i[1:].lower())
        else:
            result.append(i)
    
    return ' '.join(result)
            