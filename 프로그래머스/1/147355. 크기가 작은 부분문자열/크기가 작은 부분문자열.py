def solution(t, p):
    l_p = len(p)
    candi_list = []
    cnt = 0
    for i in range(len(t)):
        candi = t[i:i+l_p]
        if len(candi) == l_p:
            candi_list.append(int(candi))
    answer = sum(i <= int(p) for i in candi_list)
    return answer