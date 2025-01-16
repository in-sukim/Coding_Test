import sys

N = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))

stack = []
order = 1
for student in students:
  stack.append(student)
  while stack and stack[-1] == order:
    stack.pop()
    order += 1
if stack:
  print('Sad')
else:
  print("Nice")