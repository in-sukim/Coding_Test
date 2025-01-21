def solution(s):
    s_list = list(map(int, s.split()))
    s_list.sort()
    result = str(s_list[0])+ ' ' + str(s_list[-1])
    return result
    
    
    