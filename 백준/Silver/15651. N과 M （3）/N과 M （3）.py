import sys

n,m = map(int, sys.stdin.readline().split())
result = []
def back():
  if len(result) == m:
    print(*result)
    return
  for i in range(1, n+1):
    result.append(i)
    back()
    result.pop()
back()