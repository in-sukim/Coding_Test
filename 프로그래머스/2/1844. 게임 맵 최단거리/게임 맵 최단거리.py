from collections import deque

def bfs(maps):
    n,m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque([(0,0)])
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m-1:
            return visited[x][y]
        
        for dx,dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return -1
    

def solution(maps):
    return bfs(maps)