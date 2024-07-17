def solution(n):
    start, end , cnt = 1, 1, 0
    s = 1
    while end <= n:
        if s == n:
            s -= start
            cnt += 1
            start += 1
        elif s < n:
            end += 1
            s += end
        elif s > n:
            s -= start
            start += 1
    return cnt