def solution(arr):
    if len(arr) == 0:
        return [-1]
    min_num = min(arr)
    for i in range(len(arr)):
        if arr[i] == min_num:
            arr.pop(i)
            return arr