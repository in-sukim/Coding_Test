def solution(wallpaper):
    h, w = len(wallpaper), len(wallpaper[0])
    for i in wallpaper:
        print(i)
    print()
    
    point_list = []
    for row in range(h):
        for col in range(w):
            if wallpaper[row][col] == '#':
                point_list.append([row, col])
    min_x = 51
    max_x = 0
    min_y = 51
    max_y = 0
    
    for point in point_list:
        min_x = min(min_x, point[0])
        max_x = max(max_x, point[0])
        min_y = min(min_y, point[1])
        max_y = max(max_y, point[1])
    return [min_x, min_y, max_x+1, max_y+1]
        