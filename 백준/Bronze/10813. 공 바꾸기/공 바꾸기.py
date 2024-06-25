n, m = map(int, input().split())
bucket = [i+1 for i in range(n)]

for _ in range(m):
  i, j = map(int,input().split())
  i_num, j_num = bucket[i-1], bucket[j-1]
  bucket[i-1] = j_num
  bucket[j-1] = i_num
print(*bucket)