def find_mat(x,y,park,n):
    h, w = len(park), len(park[0])
    if x+n <= h and y+n <= w:
        for i in range(x, x+n):
            for j in range(y, y+n):
                if park[i][j] != '-1':
                    return False
        return True
    return False
    
def solution(mats, park):
    h, w = len(park), len(park[0])
    result = []
    for row in range(h):
        for col in range(w):
            for mat in mats:
                if find_mat(row,col,park, mat):
                    result.append(mat)
    if not result:
        return -1
    return max(result)
                