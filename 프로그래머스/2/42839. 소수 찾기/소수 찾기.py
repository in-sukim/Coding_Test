import math
from itertools import permutations
def solution(numbers):
    num_list = []
    for i in range(1, len(numbers)+1):
        value = [int(''.join(i)) for i in list(permutations(numbers, i))]
        num_list.extend(value)
    num_list = list(set(num_list))
    print(num_list)
    
    cnt = 0 
    for num in num_list:
        if num not in [0,1]:
            flag = True
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    flag = False
                    break
            if flag:
                print(num)
                cnt += 1
    return cnt
    