import sys
input = sys.stdin.readline

n, m = map(int,input().split())

a = [input().strip() for _ in range(n)]
b = [input().strip() for _ in range(m)]

answer = list(set(a).intersection(b))
answer.sort()
print(len(answer))
for i in answer:
  print(i)