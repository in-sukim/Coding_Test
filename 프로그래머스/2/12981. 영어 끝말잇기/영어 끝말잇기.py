def solution(n, words):
    answer = []
    words_list = [words[0]]
    for i in range(1, len(words)):
        if words[i] not in words_list and words_list[-1][-1] == words[i][0]:
            words_list.append(words[i])
        elif words[i] in words_list or words_list[-1][-1] != words[i][0]:
            print(words_list[-1], words[i])
            num = i % n
            answer.append(num+1)
            answer.append((i // n) + 1)
            break
            
    if not len(answer):
        return [0,0]
    else:
        return answer