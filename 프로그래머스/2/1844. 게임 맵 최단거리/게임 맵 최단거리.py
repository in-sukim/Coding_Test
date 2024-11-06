from collections import deque

def bfs(x,y,maps):
    h, w = len(maps), len(maps[0])
    move = [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque([(x,y)])
    while q:
        a,b = q.popleft()
        for move_x, move_y in move:
            nx = a + move_x
            ny = b + move_y
            if 0 <= nx < h and 0 <= ny < w:
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[a][b] + 1
                    q.append((nx,ny))
    return maps[h-1][w-1]
    
def solution(maps):
    answer = bfs(0,0,maps)
    return -1 if answer == 1 else answer