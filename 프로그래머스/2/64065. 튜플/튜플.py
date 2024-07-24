from collections import Counter
def solution(s):
    answer = []
    a = []
    a = s.replace("{","").replace("}","").split(",")
    c = Counter(a).most_common()
    
    for i in range(len(c)):
        answer.append(int(c[i][0]))
    return answer