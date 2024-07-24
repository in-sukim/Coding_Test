from itertools import permutations
def solution(k, dungeons):
    entry_list = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    
    answer = []
    for entry in entry_list:
        P = k
        cnt = 0
        for dengeon in entry:
            need_p, p = dungeons[dengeon]
            if P >= need_p:
                P -= p
                cnt += 1
            else:
                break
        answer.append(cnt)
    return max(answer)