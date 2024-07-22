from collections import defaultdict
def solution(clothes):
    clothes_dic = defaultdict(list)

    for name, type in clothes:
        clothes_dic[type].append(name)

    answer = 1
    clothes_list = list(map(len, clothes_dic.values()))
    for i in clothes_list:
        answer *= i+1
    return answer-1