def solution(N, stages):
    result = {}
    l = len(stages)
    
    for i in range(1, N+1):
        if l != 0:
            cnt_num = stages.count(i)
            result[i] = cnt_num / l
            l -= cnt_num
        else:
            result[i] = 0
    return sorted(result, key = lambda x:-result[x])