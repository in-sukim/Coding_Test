def solution(board, moves):
    cnt = 0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            pick = board[i][move-1]
            if pick:
                if bucket and bucket[-1] == pick:
                    bucket.pop(-1)
                    cnt += 2
                else:
                    bucket.append(pick)
                board[i][move-1] = 0
                break
    return cnt