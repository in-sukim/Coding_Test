def solution(d, budget):
    d.sort()
    
    for idx, i in enumerate(d):
        budget -= i
        
        if budget < 0:
            return idx
    return len(d)