def solution(arr1, arr2):
    rows, cols = len(arr1), len(arr1[0])
    
    answer = []
    for row in range(rows):
        col_list = []
        for col in range(cols):
            col_list.append(arr1[row][col] + arr2[row][col])
        answer.append(col_list)
    return answer