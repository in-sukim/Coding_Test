from collections import defaultdict
def solution(genres, plays):
    g_dict = defaultdict(int)
    p_dict = defaultdict(list)
    
    for idx, (g, p) in enumerate(zip(genres, plays)):
        g_dict[g] += p
        p_dict[g].append([idx, p])
    
    g_dict = dict(sorted(g_dict.items(), key=lambda x: x[1], reverse=True))
    
    result = []
    for genre in g_dict:
        for idx, p in sorted(p_dict[genre], key=lambda x: (-x[1], x[0]))[:2]:
            result.append(idx)
    return result
    