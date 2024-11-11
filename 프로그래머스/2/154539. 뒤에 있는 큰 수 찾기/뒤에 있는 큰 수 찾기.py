def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    
    for idx in range(len(numbers)):
        target = numbers[idx]
        
        while stack and numbers[stack[-1]] < target:
            answer[stack.pop()] = target
        stack.append(idx)
    return answer