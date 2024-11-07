from collections import Counter
def solution(topping):
    answer = 0
    old = Counter(topping)
    bro = set()
    
    for i in topping:
        old[i] -= 1
        bro.add(i)

        if old[i] == 0:
            old.pop(i)
        if len(old) == len(bro):
            answer += 1
    return answer