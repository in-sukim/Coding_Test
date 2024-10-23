def solution(a, b, n):
    total = 0
    while n >= a:
        plus = (n // a) * b
        n %= a
        n += plus
        total += plus
    
    return total