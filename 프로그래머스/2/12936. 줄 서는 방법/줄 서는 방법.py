def solution(n, k):
    numbers = list(range(1, n+1))
    answer = []
    k -= 1
    
    factorial = 1
    for i in range(1, n):
        factorial *= i
    
    for i in range(n-1, 0, -1):
        index = k // factorial
        answer.append(numbers.pop(index))
        k %= factorial
        factorial //= i

    answer.append(numbers[0])
    
    return answer