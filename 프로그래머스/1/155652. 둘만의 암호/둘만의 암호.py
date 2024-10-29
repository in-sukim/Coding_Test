def solution(s, skip, index):
    alpha = ''.join([chr(i) for i in range(97, 123) if chr(i) not in skip])
    answer = ""
    for i in s:
        answer += alpha[(alpha.find(i) + index) % len(alpha)]
    return answer