def solution(n):
    answer = ''
    n = list(str(n))
    n.sort(reverse = True)
    return int(''.join(n))