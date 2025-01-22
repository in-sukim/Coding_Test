import sys

n,m = map(int, sys.stdin.readline().split())
result = []

def back(start) :
  if len(result) == m:
    print(' '.join(map(str, result)))
    return
  for i in range(start, n+1):
   if i not in result:
     result.append(i)
     back(i+1)
     result.pop()
back(1)