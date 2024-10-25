def divisor(n):
    result = set()
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return len(result)

def solution(number, limit, power):
    divisor_list = [1]
    for i in range(2, number+1):
        divisor_list.append(divisor(i))
    
    cnt = 0
    for i in divisor_list:
        if i > limit:
            i = power
        cnt += i
    return cnt