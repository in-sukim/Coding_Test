from collections import defaultdict, Counter
def solution(want, number, discount):
    total_num = sum(number)
    dic = defaultdict(int)
    
    for w,n in zip(want, number):
        dic[w] += n
    dic = Counter(dic)
    cnt = 0
    for i in range(len(discount) - total_num + 1):
        candi_dis = Counter(discount[i:i+total_num])
        dic_diff = dic - candi_dis
        if not dic_diff:
            cnt += 1
        
    return cnt