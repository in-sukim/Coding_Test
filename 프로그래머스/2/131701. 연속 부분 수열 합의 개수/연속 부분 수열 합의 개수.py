def solution(elements):
    answer = []
    l = len(elements)
    for i in range(1,l+1):
        start = 0
        end = (start + i)
        while start < l:
            if end > l:
                end = int(end/l)
            if start <= end:
                value = sum(elements[start:end])
            else:
                value = sum(elements[start:] + elements[0:end])
            if value > 0:
                answer.append(value)
            start += 1
            end += 1
    return len(set(answer))
