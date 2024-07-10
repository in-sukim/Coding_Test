import sys
from collections import deque

test_n = int(input())

for _ in range(test_n):
  n, m = map(int,input().split())
  weights = list(map(int, input().split()))
  orders = [i for i in range(n)]
  q = deque()
  for weight, order in zip(weights, orders):
    q.append((weight, order))
  result = []
  while q:
    max_weight = max(q)
    c_weight, c_order = q.popleft()
    if c_weight < max_weight[0]:
      q.append((c_weight, c_order))
    elif c_weight == max_weight[0]:
      result.append(c_order)
  answer = result.index(m) + 1
  print(answer)
    