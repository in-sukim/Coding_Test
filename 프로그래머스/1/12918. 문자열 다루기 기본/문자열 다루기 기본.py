def solution(s):
    answer = True
    print(len(s))
    if len(s) not in [4,6]:
        return False
    
    for i in s:
        if not i.isdigit():
            return False
    return True
