from collections import Counter
def solution(participant, completion):
    parti_counter = Counter(participant)
    comple_counter = Counter(completion)
    return list((parti_counter - comple_counter).keys())[0]