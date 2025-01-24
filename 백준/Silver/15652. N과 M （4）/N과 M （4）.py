import sys

n,m = map(int, sys.stdin.readline().split())
result = []

def back(start):
  if len(result) == m:
    print(' '.join(map(str, result)))
    return
    
  for i in range(start, n+1):
    result.append(i)
    back(i)
    result.pop()

back(1)