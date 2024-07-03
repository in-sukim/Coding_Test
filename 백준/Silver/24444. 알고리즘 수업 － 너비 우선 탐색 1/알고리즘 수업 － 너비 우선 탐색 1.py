from collections import deque

n,m,r = map(int,input().split())
visited = [0] * (n+1)

graph = [[] for _ in range(n+1)]

order = 1
def bfs(graph, start, visited):
  global order
  q = deque([start])
  visited[start] = order

  while q:
    v = q.popleft()
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        order += 1
        visited[i] = order
        
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)


for i in range(n+1):
  graph[i].sort()

        
bfs(graph, r, visited)

for i in range(1, n+1):
  print(visited[i])