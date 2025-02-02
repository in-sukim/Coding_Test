def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if not visited[com]:
            dfs(n, computers, com, visited)
            answer += 1
    return answer
            
    
def dfs(n, computers, com, visited):
    visited[com] = True
    for node in range(n):
        if node != com and computers[com][node] == 1:
            if not visited[node]:
                dfs(n, computers, node, visited)