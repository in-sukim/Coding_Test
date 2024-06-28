import sys
input = sys.stdin.readline

n,m = map(int,input().split())
mat = [input().strip() for _ in range(n)]

wb = 'WBWBWBWB'
bw = 'BWBWBWBW'
wb_mat = [wb,bw,wb,bw,wb,bw,wb,bw]
bw_mat = [bw,wb,bw,wb,bw,wb,bw,wb]

def check(i,j):
  result_w = 0
  result_b = 0
  for di in range(8):
    for dj in range(8):
      ni,nj = i + di, j + dj
      if mat[ni][nj] != wb_mat[di][dj]:
        result_w += 1
      if mat[ni][nj] != bw_mat[di][dj]:
        result_b += 1
  return min(result_w, result_b)

result = 1000000
for i in range(n-7):
  for j in range(m-7):
    result = min(result, check(i,j))

print(result)
      