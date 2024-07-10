import sys
from collections import deque, defaultdict

number = input().strip()
checked = [0] * 10

for i in number:
  if i == '6' or i == '9':
    if checked[6] <= checked[9]:
      checked[6] += 1
    else:
      checked[9] += 1

  else:
    checked[int(i)] += 1
print(max(checked))