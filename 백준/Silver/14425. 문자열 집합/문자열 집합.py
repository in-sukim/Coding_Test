from collections import Counter

n,m = map(int, input().split())

s = [input() for _ in range(n)]
finds = [input() for _ in range(m)]

answer = 0
for find in finds:
  if find in s:
    answer += 1
print(answer)