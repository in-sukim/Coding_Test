def solution(s):
    stage = 0
    remove_zero = 0
    while int(s) > 1:
        remove_zero += s.count('0')
        stage += 1
        s = s.replace('0','')
        s = format(len(s), 'b')
    return [stage, remove_zero]