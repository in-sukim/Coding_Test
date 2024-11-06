def solution(n, left, right):
    result = []     
    for i in range(left, right + 1):
        row = i // n
        col = i % n   
        value = max(row + 1, col + 1)
        result.append(value)
    return result