import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
for _ in range(n):
  row = list(map(int, input().split()))
  graph.append(row)
  
k = int(input())

for _ in range(k):
  answer = 0
  i,j,x,y = map(int, input().split())
  for row in range(i-1, x):
    for col in range(j-1, y):
      answer += graph[row][col]
  print(answer)