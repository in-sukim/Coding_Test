def solution(s):
    remove_zero = 0
    cnt = 0
    while len(s) > 1:
        cnt_zero = s.count('0')
        remove_zero += cnt_zero
        cnt += 1
        before_remove_zero_l = len(s) - cnt_zero
        s = bin(before_remove_zero_l)[2:]
    return [cnt, remove_zero]
        