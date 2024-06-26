matrix = [[0] * 9 for _ in range(9)]

max_num = 0
max_row = 0
max_col = 0
for row in range(9):
  rows = list(map(int, input().split()))
  for col in range(9):
    if max_num < rows[col]:
      max_num = rows[col]
      max_row = row
      max_col = col
    matrix[row][col] = rows[col]
print(max_num)
print(max_row + 1, max_col + 1)