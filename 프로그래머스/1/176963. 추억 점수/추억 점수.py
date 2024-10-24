def solution(name, yearning, photo):
    answer = []
    for i in photo:
        temp = 0
        for j in i:
            if j in name:
                temp += yearning[name.index(j)]
        answer.append(temp)
    return answer