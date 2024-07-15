import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arrays = list(map(int, input().split()))

end = 0
sum_value = 0
cnt = 0

for start in range(n):
  while sum_value < m and end < n:
    sum_value += arrays[end]
    end += 1
  if sum_value == m:
    cnt += 1
  sum_value -= arrays[start]

print(cnt)
