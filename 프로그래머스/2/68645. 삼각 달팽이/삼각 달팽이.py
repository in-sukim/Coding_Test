# 1 2 3 4 5 6 7 8 9 10
def solution(n):    
    move = [(1,0),(0,1),(-1,-1)]
    answer = [[0 for _ in range(n)] for _ in range(n)]

    num = n * (n+1) // 2
    
    x,y = 0,0
    idx = 0
    answer[x][y] = 1
    
    for i in range(2, num+1):
        dx, dy = move[idx % 3]
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 or answer[nx][ny] != 0:
            idx += 1
            dx, dy = move[idx % 3]
            nx = x + dx
            ny = y + dy
        x = nx
        y = ny
        answer[x][y] = i
    return [i for item in answer for i in item if i != 0]
    