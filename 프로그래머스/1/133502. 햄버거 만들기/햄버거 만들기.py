def solution(ingredient):
    ingred = []
    cnt = 0
    for i in ingredient:
        ingred.append(i)
        if ingred[-4:] == [1,2,3,1]:
            cnt += 1
            del ingred[-4:]
    return cnt
            