def solution(price, money, count):
    diff = 0
    for i in range(1, count+1):
        diff += price * i
    if money < diff:
        return diff - money
    else:
        return 0