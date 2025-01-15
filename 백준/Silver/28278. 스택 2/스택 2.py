import sys

N = int(sys.stdin.readline())
stack = []

def find_command(values, stack):
  if values[0] == 1:
    stack.append(values[1])
  elif values[0] == 2:
    if stack:
      print(stack.pop(-1))
    else:
      print(-1)
  elif values[0] == 3:
    print(len(stack))
  elif values[0] == 4:
    if not stack:
      print(1)
    else:
      print(0)
  else:
    if stack:
      print(stack[-1])
    else:
      print(-1)
  
for i in range(N):
  values = list(map(int, sys.stdin.readline().split()))
  find_command(values, stack)
  