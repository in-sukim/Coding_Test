import sys
import re

while True:
  string = input()
  if string == '.':
    break
  stack = []
  flag = 'yes'
  for i in string:
    if i == '(' or i == '[':
      stack.append(i)
    elif i == ')' or i ==']':
      if not stack:
        flag = 'no'
        break
      if i == ')' and stack[-1] == '(':
        stack.pop()
      elif i == ']' and stack[-1] == '[':
        stack.pop()
      else:
        flag = 'no'
        break
  if stack:
    flag = 'no'
  print(flag)