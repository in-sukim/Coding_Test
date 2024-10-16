def solution(absolutes, signs):
    signs = [1 if i == True else -1 for i in signs]
    return sum([a * s for a,s in zip(absolutes, signs)])