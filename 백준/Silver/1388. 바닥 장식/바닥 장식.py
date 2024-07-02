n,m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
board = []
for _ in range(n):
  row = list(input())
  board.append(row)

def dfs(board, x, y, visited):
  visited[x][y] = True

  if board[x][y] == '-':
    if y + 1 < m and board[x][y+1] == '-' and visited[x][y+1] == False:
      dfs(board, x, y+1, visited)
  elif board[x][y] == '|':
    if x + 1 < n and board[x+1][y] == '|' and visited[x+1][y] == False:
      dfs(board, x+1, y, visited)

answer = 0

for i in range(n):
  for j in range(m):
    if visited[i][j] == False:
      answer += 1
      dfs(board, i, j, visited)
print(answer)
  
  