def solution(a, b):
    start,end=  0, 0
    if a <= b:
        start = a
        end = b
    else:
        start = b
        end = a
    answer = 0
    for i in range(start, end + 1):
        answer += i
    return answer 