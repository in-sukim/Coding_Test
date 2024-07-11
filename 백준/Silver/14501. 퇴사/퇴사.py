import sys
input = sys.stdin.readline

n = int(input())
T, P = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
for i in range(n):
  t, p = map(int, input().split())
  T[i] = t
  P[i] = p

for i in range(len(T) - 2, -1, -1):
  if T[i] + i <= n:
    dp[i] = max(dp[i+1], P[i] + dp[T[i] + i])
  else:
    dp[i] = dp[i+1]
print(dp[0])