from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[-1] * 102 for _ in range(102)]
    
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] == 0:
                    field[i][j] = 0
                else:
                    field[i][j] = 1
    item = (itemX, itemY)
    visited = [[False] * 102 for _ in range(102)]
    q = deque([(characterX * 2, characterY * 2)])
    visited[characterX * 2][characterY * 2] = True
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if field[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx,ny))
                field[nx][ny] = field[x][y] + 1
                visited[nx][ny] = True
    return field[itemX * 2][itemY * 2] // 2