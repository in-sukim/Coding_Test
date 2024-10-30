def solution(board, h, w):
    target_col = board[h][w]
    moves = [(-1,0), (1,0), (0,-1),(0,1)]
    cnt = 0
    start_h, start_w = h, w
    n = len(board)
    
    for move in moves:
        next_h = start_h + move[0]
        next_w = start_w + move[1]
        if 0 <= next_h < n and 0 <= next_w < n:
            if board[next_h][next_w] == board[start_h][start_w]:
                cnt += 1
    return cnt