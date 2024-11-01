def solution(park, routes):
    # 방향 dictionary
    move_dic = {
        'N' : (-1,0),
        'S' : (1,0),
        'W' : (0, -1),
        'E' : (0,1)
    }
    # 가로,세로 길이
    h,w = len(park), len(park[0])
    
    
    # 시작점 찾기
    x,y = 0,0
    for row in range(h):
        for col in range(w):
            if park[row][col] == 'S':
                x,y = row, col
    
    for route in routes:
        direction, num = route.split(' ')
        dx,dy = move_dic[direction]
        # 횟수만큼 방향 이동 했을 때 범위 벗어나는지 확인
        if 0 <= x + (dx * int(num)) < h and 0 <= y + (dy * int(num)) < w:
            flag = True
            # num만큼 이동
            temp_x, temp_y = x, y
            for _ in range(int(num)):
                nx = temp_x + dx
                ny = temp_y + dy
                if park[nx][ny] == 'X':
                    flag = False
                    break
                else:
                    temp_x = nx
                    temp_y = ny
            if flag:
                x += dx * int(num)
                y += dy * int(num)
            else:
                x = x
                y = y
    return [x,y]
                