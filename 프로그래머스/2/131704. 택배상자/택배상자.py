def solution(order):
    answer = 0
    temp = []
    for idx, num in enumerate(order):
        temp.append(idx+1)
        while temp and temp[-1] == order[answer]:
            temp.pop()
            answer += 1
    return answer