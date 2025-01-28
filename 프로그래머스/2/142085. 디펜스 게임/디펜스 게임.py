import heapq

def solution(n, k, enemy):
    
    answer = 0
    heap = []
    sum_enemy = 0
    for i in enemy:
        heapq.heappush(heap, -i)
        sum_enemy += i
        if sum_enemy > n:
            if k == 0:
                break
            max_value = -heapq.heappop(heap)
            sum_enemy -= max_value
            k -= 1
        answer += 1
    return answer
