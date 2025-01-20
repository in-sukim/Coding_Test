import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque()
for i in range(1, N+1):
  q.append(i)

idx =0
while len(q) > 1:
  if idx % 2 == 0:
    q.popleft()
  else:
    q.append(q.popleft())
  idx += 1
print(q[0])