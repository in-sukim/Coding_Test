from collections import defaultdict
def solution(clothes):
    clothes_dic = defaultdict(list)
    for name, category in clothes:
        clothes_dic[category].append(name)
    
    possible =list(map(lambda x: len(x)+1, clothes_dic.values()))
    result = 1
    for p in possible:
        result *= p
    return result - 1