def solution(n, m, section):
    paint = [section[0]]
    cnt = 1
    
    for idx in range(1, len(section)):
        if section[idx] - paint[-1] < m:
            pass
        else:
            paint.append(section[idx])
            cnt += 1
    return cnt