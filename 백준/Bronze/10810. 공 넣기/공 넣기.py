n, m = map(int, input().split())

bucket = [0] * n

for i in range(m):
  i,j,k = map(int, input().split())
  for num in range(i-1, j):
    bucket[num] = k
print(*bucket)