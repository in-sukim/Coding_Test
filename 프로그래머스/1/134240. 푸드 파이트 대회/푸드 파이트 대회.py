def solution(food):
    answer = ''
    for idx, i in enumerate(food):
        if idx > 0:
            answer += str(idx) * (i//2)
    return answer + '0' + answer[::-1]