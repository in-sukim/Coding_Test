def solution(s, n):
    print(ord('a'), ord('z'))
    print(ord('A'), ord('Z'))
    
    answer = ''
    for i in s:
        if i != ' ':
            lower_or_upper = i.islower()
            if lower_or_upper:
                if ord(i) + n > 122:
                    answer += chr(ord(i) + n - 26)
                else:
                    answer += chr(ord(i) + n)
            else:
                if ord(i) + n > 90:
                    answer += chr(ord(i) + n - 26)
                else:
                    answer += chr(ord(i) + n)
        else:
            answer += ' '
    return answer
                    