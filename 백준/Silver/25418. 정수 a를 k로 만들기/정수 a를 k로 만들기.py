from collections import deque

A,K = map(int, input().split())

def bfs(A,K):
  N = 0
  q = deque()
  q.append((A,N))
  visited = set()
  visited.add(A)

  while q:
    a,n = q.popleft()
    if a == K:
      return n
      
    type_1 = a + 1
    type_2 = a * 2
    N = n + 1

    if type_1 not in visited and type_1 <= K:
      q.append((type_1, N))
      visited.add(type_1)
    if type_2 not in visited and type_2 <= K:
      q.append((type_2, N))
      visited.add(type_2)
    
print(bfs(A,K))