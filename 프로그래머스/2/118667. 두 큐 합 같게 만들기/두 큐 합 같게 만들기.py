from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(q1)
    s2 = sum(q2)
    
    if (s1 + s2) % 2 == 1:
        return -1
    lim = (len(q1) + len(q2)) * 2
    cnt = 0
    while s1 != s2:
        if cnt >= lim:
            return -1
        while s1 > s2:
            tmp = q1.popleft()
            q2.append(tmp)
            s1 -= tmp
            s2 += tmp
            cnt += 1
        while s1 < s2:
            tmp = q2.popleft()
            q1.append(tmp)
            s1 += tmp
            s2 -= tmp
            cnt += 1
    return cnt