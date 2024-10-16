def solution(num):
    if num == 0:
        return 0
    cnt = 0 
    while num > 1:
        if cnt == 499:
            return -1
        cnt += 1
        if num % 2:
            num = (num * 3) + 1
        else:
            num = num // 2
    return cnt
        