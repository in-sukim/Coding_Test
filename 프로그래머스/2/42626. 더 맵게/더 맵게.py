import heapq
def solution(scoville, k):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    
    cnt = 0
    while len(heap) >= 2:
        if heap[0] >= k:
            return cnt
        
        min_value = heapq.heappop(heap)
        min_next_value = heapq.heappop(heap)
        new_scoville = min_value + (min_next_value * 2)
        heapq.heappush(heap, new_scoville)
        cnt += 1
    
    if heap and heap[0] >= k:
        return cnt
    return -1

        
    