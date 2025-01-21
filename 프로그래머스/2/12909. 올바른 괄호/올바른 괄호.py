def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
    if stack:
        return False
    else:
        return True