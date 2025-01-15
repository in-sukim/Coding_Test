import sys

def is_parenthesis(strings):
  stack = []
  for i in strings:
    if i == '(':
      stack.append(i)
    else:
      if stack:
        if stack[-1] == '(':
          stack.pop(-1)
      else:
        return "NO"
  return "YES" if not stack else "NO"


N = int(sys.stdin.readline())
for i in range(N):
  strings = input()
  print(is_parenthesis(strings))
  
    