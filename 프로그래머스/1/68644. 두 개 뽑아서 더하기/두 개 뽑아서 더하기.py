from itertools import combinations
def solution(numbers):
    answer = []
    comb_list = [sum(i) for i in list(combinations(numbers, 2))]
    if len(comb_list) > 0:
        answer.extend(comb_list)
    answer = list(set(answer))
    answer.sort()
    return answer