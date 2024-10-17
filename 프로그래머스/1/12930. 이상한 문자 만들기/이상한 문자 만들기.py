def solution(s):
    s_split = s.split(' ')
    answer = []
    for i in s_split:
        tmp = ''
        for j in range(len(i)):
            if j % 2:
                tmp += i[j].lower()
            else:
                tmp += i[j].upper()
        answer.append(tmp)
    return ' '.join(answer)
                
            
        
            