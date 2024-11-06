from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()

    for i in cities:
        i = i.lower()
        if i in q:
            answer += 1
            q.remove(i)
            q.append(i)
        else:
            answer += 5
            q.append(i)
            if len(q) > cacheSize:
                q.popleft()
    return answer