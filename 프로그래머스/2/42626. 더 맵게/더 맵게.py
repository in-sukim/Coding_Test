import heapq

def solution(scoville, K):
    # 이미 모든 음식이 K 이상인 경우를 먼저 체크
    if min(scoville) >= K:
        return 0
        
    # 길이가 2 미만이면서 K를 만족하지 못하면 불가능
    if len(scoville) < 2:
        return -1
    
    heapq.heapify(scoville)
    cnt = 0
    
    # 힙의 크기를 미리 저장
    heap_size = len(scoville)
    
    while heap_size >= 2:
        # 최소값이 이미 K 이상이면 종료
        if scoville[0] >= K:
            return cnt
            
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        
        # 두 번째로 작은 값도 K 이상이면 나머지는 모두 K 이상
        if min_2 >= K:
            # 마지막 계산 후 결과가 K 이상이면 성공
            if min_1 + (min_2 * 2) >= K:
                return cnt + 1
            return -1
            
        new_scoville = min_1 + (min_2 * 2)
        heapq.heappush(scoville, new_scoville)
        cnt += 1
        heap_size -= 1
        
        # 최적화: 새로 만든 값이 K보다 작고, 힙 크기가 1이면 더 이상 불가능
        if new_scoville < K and heap_size == 1:
            return -1
    
    # 마지막 확인
    return cnt if scoville[0] >= K else -1