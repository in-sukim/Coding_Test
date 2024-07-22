def solution(citations):
    answer = 0
    citations.sort(reverse =True)
    
    for h in range(len(citations)):
        if h >= citations[h]:
            return h
    return len(citations)