import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

q = deque(enumerate(map(int, input().split())))
answer = []

while q:
  idx, current = q.popleft()
  answer.append(idx + 1)
  if current > 0:
    q.rotate(-(current-1))
  else:
    q.rotate((-current))
print(*answer)