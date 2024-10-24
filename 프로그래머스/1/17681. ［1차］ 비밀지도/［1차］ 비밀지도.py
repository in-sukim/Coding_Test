def solution(n, arr1, arr2):
    arr1 = [bin(i)[2:].zfill(n) for i in arr1]
    arr2 = [bin(i)[2:].zfill(n) for i in arr2]
    answer = []
    
    for i in range(n):
        temp = ''
        for j in range(n):
            sum_value = int(arr1[i][j]) + int(arr2[i][j])
            if sum_value > 0:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer