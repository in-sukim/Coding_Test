def solution(s):
    s = list(map(int, s.split(' ')))
    s.sort()
    min_value, max_value = str(s[0]), str(s[-1])
    return min_value + ' ' + max_value