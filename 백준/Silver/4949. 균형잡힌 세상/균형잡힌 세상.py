import sys


def brackets(lines):
    stack = []
    for i in lines:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack:
                return "no"
            elif stack[-1] == "(":
                stack.pop()
            else:
                return "no"
        elif i == "]":
            if not stack:
                return "no"
            elif stack[-1] == "[":
                stack.pop()
            else:
                return "no"
    if not stack:
        return "yes"
    else:
        return "no"


answer = []
while True:
    line = sys.stdin.readline()
    if line == ".\n":
        break
    answer.append(brackets(line))

print("\n".join(answer))