import re
def solution(files):
    answer = []
    file = []

    for idx, i in enumerate(files):
        number = re.findall("\d+", i)
        head = i[:i.index(number[0])].lower()
        file.append([head, int(number[0]), idx])

    file.sort(key = lambda x: [x[0], x[1], x[2]])
    for i in file:
        answer.append(files[i[-1]])
    return answer