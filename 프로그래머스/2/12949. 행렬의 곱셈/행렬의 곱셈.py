def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            arr2_temp = []
            for k in range(len(arr2)):
                arr2_temp.append(arr2[k][j])
            value = sum([i * j for i,j in zip(arr1[i], arr2_temp)])
            temp.append(value)
        result.append(temp)
    return result