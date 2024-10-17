from itertools import combinations
def solution(number):
    cnt = 0
    candi = list(combinations(number,3))
    for i in candi:
        if sum(i) == 0:
            cnt += 1
    return cnt