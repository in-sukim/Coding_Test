from itertools import product
def solution(word):
    alpha = ["A","E","I","O","U"]
    all_alpha = []
    for i in range(1, len(alpha)+1):
        value = [''.join(i) for i in list(product(alpha, repeat = i))]
        all_alpha.extend(value)
    all_alpha.sort()

    for idx, i in enumerate(all_alpha):
        if i == word:
            return idx + 1