def solution(k, score):
    honor = []
    answer = []
    for i in score:
        if len(honor) < k:
            honor.append(i)
        else:
            min_honor = min(honor)
            min_idx = honor.index(min_honor)
            if i > min_honor:
                honor.pop(min_idx)
                honor.append(i)
        answer.append(min(honor))
    return answer