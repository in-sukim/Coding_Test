def solution(msg):
    alpha_dic = {i:idx for idx, i in enumerate([chr(i) for i in range(65, 91)], 1)}
    answer = []
    
    w = c = 0
    while True:
        c += 1
        if c == len(msg):
            answer.append((alpha_dic[msg[w:c]]))
            break
        if msg[w:c+1] not in alpha_dic:
            alpha_dic[msg[w:c+1]] = len(alpha_dic) + 1
            answer.append(alpha_dic[msg[w:c]])
            w = c
    return answer