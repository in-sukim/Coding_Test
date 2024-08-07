def solution(sequence, k):
    answer = []
    sum_value, right = 0,0
    
    for left in range(len(sequence)):
        while right < len(sequence) and sum_value < k:
            sum_value += sequence[right]
            right += 1
        if sum_value == k:
            if len(answer) == 0:
                answer = [left, right - 1]
            else:
                answer = answer if answer[1] - answer[0] <= (right - 1) - left else [left, right -1]
        sum_value -= sequence[left]
    return answer