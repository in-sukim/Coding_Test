# import math
# from collections import deque
# def solution(progresses, speeds):
#     days = deque()
#     answer = []
#     for progress, speed in zip(progresses, speeds):
#         day = (100 - progress) / speed
#         days.append(math.ceil(day))
        
#     while days:
#         c = days.popleft()
#         cnt = 1
        
#         while days and c >= days[0]:
#             days.popleft()
#             cnt += 1
#         answer.append(cnt)
#     return answer
    

import math

def solution(progresses, speeds):
    days = []
    answer = []
    for progress, speed in zip(progresses, speeds):
        day = (100 - progress) / speed
        days.append(math.ceil(day))

    cnt = 0
    before_day = days[0]
    for i in range(len(days)):
        if before_day < days[i]:
            answer.append(cnt)
            before_day = days[i]
            cnt = 0
        cnt += 1
    answer.append(cnt)


    return answer