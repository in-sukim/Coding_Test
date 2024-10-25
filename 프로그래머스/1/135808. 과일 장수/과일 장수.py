def solution(k, m, score):
    score.sort(reverse = True)
    
    answer = 0
    for idx in range(0,len(score),m):
        box = score[idx:idx+m]
        if len(box) == m:
            answer += min(box) * m
    return answer