def solution(p):
    answer = ''
    
    def divide(li):
        openCount = 0
        closeCount = 0
        for i in li:
            if (i == '('):
                openCount += 1
            else:
                closeCount += 1
            
            if (openCount == closeCount):
                u = li[ : openCount + closeCount]
                v = li[openCount + closeCount : ]
                return u, v
    
    def check(li):
        stack = list()
        for i in li:
            if (i == '('):
                stack.append(i)
            else:
                if (len(stack) > 0):
                    stack.pop()
                else:
                    return False
            
        return True
    
    def newStr(u, v):
        result.append('(')
        process(v)
        result.append(')')

        del u[0]
        del u[-1]
        for i in u:
            if (i == '('):
                result.append(')')
            else:
                result.append('(')

    def process(li):
        if (len(li) == 0):
            return
        
        u, v = divide(li)

        if (check(u)):
            result.extend(u)
            process(v)
        else:
            newStr(u, v)

    result = list()
    process(list(p))

    answer = ''.join(result)
    return answer