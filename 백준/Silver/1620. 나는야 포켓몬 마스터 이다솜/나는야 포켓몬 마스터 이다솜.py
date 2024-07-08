import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
monster_dic = defaultdict(int)

for i in range(n):
  monster = input().strip()
  monster_dic[monster] += (i+1)
monster_name = [i for i in monster_dic.keys()]

for _ in range(m):
  find = input().strip()
  if find.isalpha():
    print(monster_dic[find])
  else:
    print(monster_name[int(find) - 1])