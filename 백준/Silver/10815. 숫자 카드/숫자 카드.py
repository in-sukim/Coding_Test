import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
own_card = list(map(int, list(input().split())))
m = int(input())
find_card = list(map(int, list(input().split())))

dic = Counter(own_card)
answer = []

for i in find_card:
  if i in dic:
    answer.append(1)
  else:
    answer.append(0)
print(*answer)
