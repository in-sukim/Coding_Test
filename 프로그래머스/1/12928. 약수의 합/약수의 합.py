def solution(n):
    answer = []
    for i in range(1,n+1):
        if i not in answer:
            if n % i == 0:
                append_nums = [i, n // i]
                answer.extend(append_nums)
    return sum(set(answer))
            