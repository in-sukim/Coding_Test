from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    q = deque([1])
    distance = [0] * (n+1)
    answer = 0
    
    while q:
        cur = q.popleft()
        for node in graph[cur]:
            if not distance[node]:
                q.append(node)
                distance[node] = distance[cur] + 1
    result = distance[2:]
    return result.count(max(result))
                
        