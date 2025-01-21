import heapq
def solution(A,B):
    min_heap = []
    max_heap = []
    for i in range(len(A)):
        heapq.heappush(min_heap, A[i])
        heapq.heappush(max_heap, -B[i])
    
    answer = 0
    for i in range(len(min_heap)):
        min_value = heapq.heappop(min_heap)
        max_value = -heapq.heappop(max_heap)
        answer += min_value * max_value
    return answer