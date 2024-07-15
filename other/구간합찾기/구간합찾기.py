import sys
input = sys.stdin.readline

n = int(input())
start, end = map(int,input().split())
data = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]

for i in data:
  sum_value += i
  prefix_sum.append(sum_value)

print(prefix_sum[end] - prefix_sum[start - 1])
