def solution(board, moves):
    col = len(board[0])
    new_board = []
    picked = []
    for c in range(col):
        temp = []
        temp_pick = []
        for i in board:
            flag = True
            temp.append(i[c])
            if i[c] == 0:
                flag = False
            temp_pick.append(flag)
        new_board.append(temp[::-1])
        picked.append(temp_pick[::-1])
    
    cnt = 0
    bucket = []
    for move in moves:
        possible_pick = [idx for idx, i in enumerate(picked[move-1]) if i]
        if not len(possible_pick):
            break
        else:
            pick_idx = max(possible_pick)
        pick = new_board[move-1][pick_idx]
        if bucket and bucket[-1] == pick:
            bucket.pop(-1)
            cnt += 2
        else:
            bucket.append(pick)
        picked[move-1][pick_idx] = False
    return cnt