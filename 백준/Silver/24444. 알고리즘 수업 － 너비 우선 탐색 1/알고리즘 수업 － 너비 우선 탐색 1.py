from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
count = 1
        
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)


for i in range(1, n+1):
  graph[i].sort()

def bfs(start):
  q = deque([start])
  global count
  visited[start] = count
  count += 1

  while q:
    v = q.popleft()
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = count
        count += 1
        
bfs(r)

for i in range(1, n+1):
  print(visited[i])