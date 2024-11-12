from collections import deque

def bfs(start_x, start_y, target_map):
    n, m = len(target_map), len(target_map[0])
    visited = [[-1] * m for _ in range(n)]
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = 0
    
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while q:
        x, y = q.popleft()
            
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and target_map[nx][ny] != 'X':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    return visited

def solution(maps):
    maps = [list(row) for row in maps]
    n, m = len(maps), len(maps[0])
    
    start_x = start_y = lever_x = lever_y = end_x = end_y = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start_x, start_y = i, j
            elif maps[i][j] == 'L':
                lever_x, lever_y = i, j
            elif maps[i][j] == 'E':
                end_x, end_y = i, j
    
    from_start = bfs(start_x, start_y, maps)

    if from_start[lever_x][lever_y] == -1:
        return -1
        
    from_lever = bfs(lever_x, lever_y, maps)
    
    if from_lever[end_x][end_y] == -1:
        return -1
    
    return from_start[lever_x][lever_y] + from_lever[end_x][end_y]