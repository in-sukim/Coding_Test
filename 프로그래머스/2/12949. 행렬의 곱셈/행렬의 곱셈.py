def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        element_list = []
        for j in range(len(arr2[0])):
            element = 0
            for k in range(len(arr1[0])):
                # print(f"{i,k}, {j,k}")
                element += arr1[i][k] * arr2[k][j]
            element_list.append(element)
        answer.append(element_list)
    return answer