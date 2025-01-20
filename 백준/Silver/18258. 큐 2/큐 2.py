import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
  inputs = sys.stdin.readline().split()
  action = inputs[0]
  if action == 'push':
    q.append(int(inputs[1]))
  elif action == 'pop':
    if q:
      print(q.popleft())
    else:
      print('-1')
  elif action == 'size':
    print(len(q))
  elif action == 'empty':
    if not len(q):
      print(1)
    else:
      print(0)
  elif action == 'front':
    if q:
      print(q[0])
    else:
      print(-1)
  else:
    if q:
      print(q[-1])
    else:
      print(-1)