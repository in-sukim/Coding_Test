n, m = map(int, input().split())
bucket = [i+1 for i in range(n)]

for _ in range(m):
  i,j = map(int,input().split())
  forward_list = []
  for num in range(i-1, j):
    forward_list.append(bucket[num])
  inverse_list = forward_list[::-1]
  bucket[i-1:j] = inverse_list
print(*bucket)