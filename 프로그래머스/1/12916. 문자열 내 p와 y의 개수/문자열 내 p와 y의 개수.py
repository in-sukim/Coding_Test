def solution(s):
    s = s.lower()
    s_cnt = s.count('p')
    y_cnt = s.count('y')
    return True if s_cnt == y_cnt else False