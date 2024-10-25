def divisor(number):
    for i in range(2, int(number ** (1/2)) + 1):
        if number % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if divisor(i) == True:
            answer += 1
    return answer