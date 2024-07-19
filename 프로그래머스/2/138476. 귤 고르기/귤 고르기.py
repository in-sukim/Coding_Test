from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter=Counter(tangerine)
    sort_c=sorted(counter.items(),key=lambda x:x[1],reverse=True)
    cnt=0
    for i in sort_c:
        k-=i[1]
        answer+=1
        
        if k<=0:
            break
            
    return answer