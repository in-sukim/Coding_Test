import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    
    while len(scoville) >= 2:
        first = hq.heappop(scoville)
        if first >= K:
            hq.heappush(scoville, first)  # 다시 넣어주고
            break
            
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1
    
    # 모든 값이 K 이상인지 확인
    if scoville and scoville[0] >= K:
        return answer
    return -1