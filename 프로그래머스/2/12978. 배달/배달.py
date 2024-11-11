import heapq

INF = 100000 * 50
def solution(N, road, K):
    distance = [INF] * (N+1)
    distance[1] = 0
    
    graph = [[] for _ in range(N+1)]
    
    for route in road:
        start, end, edge = route 
        graph[start].append((end,edge))
        graph[end].append((start,edge))
    
    heap = []
    heapq.heappush(heap, (0,1))
    
    while heap:
        dis, now = heapq.heappop(heap)
        if distance[now] < dis:
            continue
        for node in graph[now]:
            if node[1] + dis < distance[node[0]]:
                distance[node[0]] = node[1] + dis
                heapq.heappush(heap, (distance[node[0]], node[0]))
    answer = 0
    for i in distance:
        if i <= K:
            answer += 1
    return answer