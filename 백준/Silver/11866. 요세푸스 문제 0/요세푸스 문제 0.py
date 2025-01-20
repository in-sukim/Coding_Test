import sys

input = sys.stdin.readline

n,k = map(int,input().split())

nums = list(range(1,n+1))

result = []
idx = 0
for i in range(n):
  idx += k - 1
  if idx >= len(nums):
    idx %= len(nums)
  result.append(str(nums.pop(idx)))

print('<{}>'.format(', '.join(result)))