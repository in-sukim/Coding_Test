import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) >= 2 and scoville[0] < K:
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        new_scoville = min_1 + (min_2 * 2)
        heapq.heappush(scoville, new_scoville)
        cnt += 1
    if scoville[0] >= K:
        return cnt
    return -1