import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
  inputs = list(map(int, sys.stdin.readline().split()))
  if inputs[0] == 1:
    q.appendleft(inputs[-1])
  elif inputs[0] == 2:
    q.append(inputs[-1])
  elif inputs[0] == 3:
    if q:
      print(q.popleft())
    else:
      print(-1)
  elif inputs[0] == 4:
    if q:
      print(q.pop())
    else:
      print(-1)
  elif inputs[0] == 5:
    print(len(q))
  elif inputs[0] == 6:
    if q:
      print(0)
    else:
      print(1)
  elif inputs[0] == 7:
    if q:
      print(q[0])
    else:
      print(-1)
  elif inputs[0] == 8:
    if q:
      print(q[-1])
    else:
      print(-1)
    
