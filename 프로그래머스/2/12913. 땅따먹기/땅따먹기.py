def solution(land):
    N = len(land)
    
    dp = [[0] * 4 for _ in range(N)]
    dp[0] = land[0][:]
    
    for i in range(1, N):
        for j in range(4):
            dp[i][j] = land[i][j] + max(
                dp[i-1][(j+1)%4],
                dp[i-1][(j+2)%4],
                dp[i-1][(j+3)%4]
            )
    return max(dp[N-1])