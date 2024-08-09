import collections

def bfs(x,y,maps,visited):
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    q = collections.deque()
    q.append((x,y))

    visited[x][y] = 1 #visited

    days = int(maps[x][y])
    while q: 
        x,y = q.popleft()

        for tx, ty in moves:
            nx = x + tx
            ny = y + ty

            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if maps[nx][ny] != 'X' and visited[nx][ny] != 1:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    days += int(maps[nx][ny])

    return days


def solution(maps):
    total = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                total.append(bfs(i,j,maps,visited))

    if total:
        return sorted(total)
    else: return [-1]