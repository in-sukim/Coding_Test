def solution(storey):
    answer = 0
    
    while storey > 0:
        button = storey % 10
        if button > 5:
            storey += (10 - button)
            answer += (10 - button)
        elif button < 5:
            storey -= button
            answer += button
        else:
            front_num = storey // 10
            if front_num % 10 >= 5:
                storey += (10 - button)
                answer += (10 - button)
            else:
                storey -= button
                answer += button
        storey //= 10
    return answer