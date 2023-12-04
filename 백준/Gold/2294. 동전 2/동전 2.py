n,k = map(int,input().split())
tokens = [int(input()) for _ in range(n)]


dp = [99999 for _ in range(k+1)]
dp[0] = 0

for token in tokens:
  for now in range(1,k+1):
    if now - token >= 0:
      dp[now] = min(dp[now], dp[now-token] + 1)

if dp[k] == 99999:
  print(-1)
else:
  print(dp[k])