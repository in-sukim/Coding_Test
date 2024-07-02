n = int(input())
con_n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(con_n):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      dfs(graph,i,visited)
  return visited

print(sum(dfs(graph,1,visited)) - 1)
  