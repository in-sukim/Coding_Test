n = int(input())
a,b = map(int, input().split())
m = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
  x,y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)


def dfs(x, num):
  global flag
  visited[x] = True
  if x == b:
    flag = True
    print(num)
  for i in graph[x]:
    if not visited[i]:
      dfs(i, num + 1)
flag = False
dfs(a,0)
if not flag:
  print(-1)