def solution(babbling):
    possible = ['aya','ye','woo','ma']
    answer = []
    for babb in babbling:
        temp = ''
        before = ''
        for b in babb:
            temp += b
            if temp in possible and before != temp:
                flag = True
                before = temp
                temp = ''
            else:
                flag = False
        answer.append(flag)
    return sum(answer)