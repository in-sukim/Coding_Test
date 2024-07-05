from itertools import permutations

s = input()

answer = set()
num = 0
for i in range(len(s)):
  for j in range(len(s)):
    if s[i:j+1] != '':  
      answer.add(s[i:j+1])
print(len(list(answer)))