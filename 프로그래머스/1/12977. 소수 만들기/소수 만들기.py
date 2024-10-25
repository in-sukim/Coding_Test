from itertools import combinations
def isPrime(number):
    for i in range(2, int(number ** (1/2)) + 1):
        if number % i == 0:
            return False
    return True

def solution(nums):
    comb = [sum(i) for i in combinations(nums, 3)]
    print(comb)
    cnt = 0
    for i in comb:
        if isPrime(i) == True:
            cnt += 1
    return cnt
    
    