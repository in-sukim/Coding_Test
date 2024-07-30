from itertools import permutations
def solution(skill, skill_trees):
    skill_order = []
    for j in range(len(skill)):
        skill_order.append(skill[0:j+1])

    cnt = 0
    for skill_name in skill_trees:
        temp = ''
        for i in skill_name:
            if i in list(skill):
                temp += i
        if temp == '':
            cnt += 1
        else: 
            if temp in skill_order:
                cnt += 1

    return cnt