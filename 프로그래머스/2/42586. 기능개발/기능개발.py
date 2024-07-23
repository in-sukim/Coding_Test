import math
from collections import deque
def solution(progresses, speeds):
    days = deque()
    answer = []
    for progress, speed in zip(progresses, speeds):
        day = (100 - progress) / speed
        days.append(math.ceil(day))
        
    while days:
        c = days.popleft()
        cnt = 1
        
        while days and c >= days[0]:
            days.popleft()
            cnt += 1
        answer.append(cnt)
    return answer
    
        