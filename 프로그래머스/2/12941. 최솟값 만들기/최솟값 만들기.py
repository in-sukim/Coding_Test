import heapq
def solution(A,B):
    a_heap = []
    b_heap = []
    
    for i in A:
        heapq.heappush(a_heap, i)
    for j in B:
        heapq.heappush(b_heap, (-j,j))
    
    answer = 0
    while a_heap:
        a_value = heapq.heappop(a_heap)
        b_value = heapq.heappop(b_heap)[1]
        answer += a_value * b_value
    return answer
        