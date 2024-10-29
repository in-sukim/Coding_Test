from collections import defaultdict
def solution(s):
    s_list = []
    cnt = 0
    same_cnt, diff_cnt = 0, 0
    for idx, i in enumerate(s):
        if len(s_list) == 0:
            s_list.append(i)
        if s_list[-1] != i:
            diff_cnt += 1
            if same_cnt == diff_cnt:
                s = s[idx+1:]
                s_list = []
                same_cnt, diff_cnt = 0,0
                cnt += 1
        elif s_list[-1] == i:
            same_cnt += 1
    if len(s_list):
        cnt += 1
        
    return cnt
            