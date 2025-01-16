import sys

N = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))

order = 1
waiting_stack = []
for student in students:
  if student == order:
    order += 1
    while waiting_stack and waiting_stack[-1] == order:
      waiting_stack.pop()
      order +=1
    continue
  else:
    if not waiting_stack:
      waiting_stack.append(student)
    else:
      if waiting_stack[-1] == order:
        waiting_stack.pop()
        order += 1
      else:
        waiting_stack.append(student)
if not waiting_stack:
  print('Nice')
else:
  for i in waiting_stack[::-1]:
    if i != order:
      print('Sad')
      break
    else:
      order += 1
  if order == N:
    print('Nice')