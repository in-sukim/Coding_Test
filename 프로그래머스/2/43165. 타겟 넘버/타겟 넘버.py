def solution(numbers,target):
    result = [0]
    cnt = 0

    for num in numbers:
        temp = []
        for i in result:
            temp.append(i - num)
            temp.append(i + num)
        result = temp
        
    for i in  result:
        if i == target:
            cnt += 1
    return cnt