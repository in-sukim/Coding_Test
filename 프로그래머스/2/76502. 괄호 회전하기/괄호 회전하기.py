def solution(s):
    cnt = 0
    for i in range(len(s)):
        rotate_s = s
        if i != 0:
            rotate_s = s[i:] + s[0:i]
        stack = []
        flag = True
        for span in rotate_s:
            if span in ['[','(','{']:
                stack.append(span)
            else:
                if len(stack) == 0:
                    flag = False
                    break
                else:
                    if (span == ']' and stack[-1] == '[') or (span == ')' and stack[-1] == '(') or (span == '}' and stack[-1] == '{'):
                        stack.pop(-1)
                        flag = True
        if flag == True and len(stack) == 0:
            cnt += 1
    return cnt