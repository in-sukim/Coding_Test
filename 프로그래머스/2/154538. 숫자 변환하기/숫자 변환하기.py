from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    q = deque([(x,0)])
    visited = set()
    visited.add(x)
    
    while q:
        current_x, cnt = q.popleft()
        for next_step in (current_x * 3, current_x * 2, current_x + n):
            if next_step == y:
                return cnt + 1
            if 1 <= next_step <= y and next_step not in visited:
                visited.add(next_step)
                q.append((next_step, cnt + 1))
    return -1