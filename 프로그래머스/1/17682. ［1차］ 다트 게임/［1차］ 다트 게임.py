def solution(dartResult):
    dartResult = dartResult.replace('10','n')
    SDT = {
        'S': 1,
        'D': 2,
        'T': 3
    }
    score = []
    
    for i in dartResult:
        if i.isdigit() or i == 'n':
            if i == 'n':
                score.append(10)
            else:
                score.append(int(i))
        elif i in SDT:
            cur_score = score.pop()
            score.append(cur_score ** SDT[i])
        elif i == '*':
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2
        elif i == '#':
            score[-1] *= -1
    return sum(score)