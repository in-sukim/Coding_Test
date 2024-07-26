from collections import deque
def solution(maps):
    n,m = len(maps), len(maps[0])
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False] * m for _ in range(n)]

    q = deque([(0,0)])
    while q:
        a,b = q.popleft()
        for move_x, move_y in move:
            nx = a + move_x
            ny = b + move_y
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx,ny))
                    maps[nx][ny] = maps[a][b] + 1
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]