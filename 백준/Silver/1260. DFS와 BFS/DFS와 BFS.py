import sys
from collections import deque

n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited1 = [False] * (n+1)
visited2 = visited1.copy()

for _ in range(m):
  u,v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

graph = list(map(sorted, graph))

def dfs(start):
  visited1[start] = True
  print(start, end = ' ')
  for node in graph[start]:
    if not visited1[node]:
      dfs(node)


def bfs(start):
  visited2[start] = True
  q = deque([start])
  
  print(start, end = ' ')
  while q:
    a = q.popleft()
    for node in graph[a]:
      if not visited2[node]:
        visited2[node] = True
        q.append(node)
        print(node, end = ' ')    

dfs(r)
print()
bfs(r)