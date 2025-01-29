import heapq
def solution(operations):
    heap = []
    for operation in operations:
        action, value = operation.split()
        value = int(value)
        
        if action == 'I':
            heapq.heappush(heap, value)
        
        elif action == 'D' and value == 1:
            if heap:
                heap.remove(max(heap))
        elif action == 'D' and value == -1:
            if heap:
                heapq.heappop(heap)
    if not len(heap):
        return [0,0]
    else:
        return [max(heap), heapq.heappop(heap)]
        
            