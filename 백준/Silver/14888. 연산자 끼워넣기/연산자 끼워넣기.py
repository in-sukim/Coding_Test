import sys

N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
max_result = -int(1e9)
min_result = int(1e9)

def back(add, sub, mul, div, sum, idx):
  global max_result, min_result
  if idx == N:
    max_result = max(max_result, sum)
    min_result = min(min_result, sum)
    return
  if add:
    back(add-1, sub, mul, div, sum + number[idx], idx+1)
  if sub:
    back(add, sub-1, mul, div, sum - number[idx], idx+1)
  if mul:
    back(add, sub, mul - 1, div, sum * number[idx], idx+1)
  if div:
    back(add, sub, mul, div - 1, int(sum / number[idx]), idx+1)

back(add, sub, mul, div, number[0], 1)
print(max_result)
print(min_result)