n,m = map(int, input().split())

matrix = [[0] * m for _ in range(n)]

current_row = 0
for i in range(n * 2):
  if (i + 1) >= n:
    current_row = i -n
  rows = list(map(int, input().split()))
  new_rows = [x + y for x,y in zip(matrix[current_row], rows)]
  matrix[current_row] = new_rows
  current_row += 1

for row in matrix:
  print(*row)
    
