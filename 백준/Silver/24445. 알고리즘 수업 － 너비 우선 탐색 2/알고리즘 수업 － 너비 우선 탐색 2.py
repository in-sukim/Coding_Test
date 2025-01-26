import sys
from collections import deque
n,m,r = map(int, sys.stdin.readline().split())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
order = 2

for i in range(m):
  u,v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

def bfs(start, visited):
  global order
  q = deque([start])
  visited[start] = 1
  while q:
    a = q.popleft()
    for node in sorted(graph[a], reverse = True):
      if not visited[node]:
        visited[node] = order
        q.append(node)
        order += 1
  return visited

bfs(r,visited)
for i in range(1,len(visited)):
  print(visited[i])
    