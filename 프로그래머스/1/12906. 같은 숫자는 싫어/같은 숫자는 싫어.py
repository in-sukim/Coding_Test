def solution(arr):
    stack = [arr[0]]
    for i in arr:
        if stack and stack[-1] != i:
            stack.append(i)
    return stack
    