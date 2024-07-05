from collections import defaultdict

n = int(input())

log = [input().split() for _ in range(n)]
log_dic = defaultdict()

for name, status in log:
  log_dic[name] = status

answer = [name for name, status in log_dic.items() if status != 'leave']

answer.sort(reverse = True)
for i in answer:
  print(i)