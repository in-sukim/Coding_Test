from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque([(0,0)])
    while q:
        cur_sum, cur_idx = q.popleft()

        if cur_idx == len(numbers):
            if cur_sum == target:
                answer += 1
        else:
            number = numbers[cur_idx]
            q.append((cur_sum + number, cur_idx + 1))
            q.append((cur_sum - number, cur_idx + 1))
    return answer