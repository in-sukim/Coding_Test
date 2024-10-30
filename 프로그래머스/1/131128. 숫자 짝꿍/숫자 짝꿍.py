from collections import Counter
def solution(X, Y):
    x_counter = Counter(X)
    y_counter = Counter(Y)
    inter_xy= dict(x_counter&y_counter)
    if not len(inter_xy):
        return '-1'
    if list(inter_xy) == ['0']:
        return '0'
    result = ''
    for i in range(9, -1, -1):
        i = str(i)
        if i in inter_xy:
            result += str(i) * inter_xy[i]
    return result