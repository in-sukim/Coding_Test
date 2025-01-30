def solution(n, results):
    graph = [[0]*n for _ in range(n)]
    for win,lose in results:
        graph[win-1][lose-1] = 1
        graph[lose-1][win-1] = -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[i][j] != 0:
                cnt += 1
        if cnt == n-1:
            answer += 1
    return answer
    