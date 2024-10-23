def solution(strings, n):
    order_string = [[idx, i[n], i] for idx, i in enumerate(strings)]
    order_string.sort(key = lambda x:(x[1],x[2]))
    answer = []
    for idx, i, j in order_string:
        answer.append(strings[idx])
    return answer