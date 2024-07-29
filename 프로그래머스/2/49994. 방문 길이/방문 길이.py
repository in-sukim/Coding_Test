def solution(dirs):
    move_dic = {"U": [1,0], "D": [-1,0], "R": [0,1], "L": [0,-1]}
    x, y = 0,0
    result = []
    for d in dirs:
        move_x, move_y = move_dic[d]
        nx = x + move_x
        ny = y + move_y
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            pass
        else:
            key_name_1 = str(x)+str(y) + ',' + str(nx)+str(ny)
            key_name_2 = str(nx)+str(ny) + ',' + str(x)+str(y)
            if key_name_1 not in result and key_name_2 not in result:
                result.append(key_name_1)
            x,y = nx, ny

    return len(result)