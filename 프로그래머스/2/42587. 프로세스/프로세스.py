import sys
from collections import deque
input = sys.stdin.readline

def solution(priorities, location):
    pri_order = sorted(priorities, reverse = True)
    priorities = [[idx, i] for idx,i in enumerate(priorities)]
    q = deque(priorities)

    answer = []
    while q:
        idx, v = q.popleft()
        if v == pri_order[0]:
            pri_order.pop(0)
            answer.append(idx)

        else:
            q.append([idx, v])
    for idx, value in enumerate(answer):
        if value == location:
            return idx + 1 