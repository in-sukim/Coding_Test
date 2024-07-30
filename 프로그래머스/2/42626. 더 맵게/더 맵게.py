import heapq
def solution(scovile, K):
    heapq.heapify(scovile)
    cnt = 0
    while scovile[0] < K:
        if len(scovile) < 2 :
            return - 1
        first_min = heapq.heappop(scovile)
        second_min = heapq.heappop(scovile)
        new_scovile = first_min + (second_min * 2)
        heapq.heappush(scovile, new_scovile)
        cnt += 1

    return cnt