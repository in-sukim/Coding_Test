def solution(lottos, win_nums):
    
    zero_num = len([i for i in lottos if i == 0])
    match_num = set(lottos).intersection(set(win_nums))
    
    min_num = len(match_num)
    max_num = min_num + zero_num
    
    rank_dic = {
        6 : 1,
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5
    }
    if max_num in rank_dic:
        max_num = rank_dic[max_num]
    else:
        max_num = 6
        
    if min_num in rank_dic:
        min_num = rank_dic[min_num]
    else:
        min_num = 6
    return [max_num, min_num]