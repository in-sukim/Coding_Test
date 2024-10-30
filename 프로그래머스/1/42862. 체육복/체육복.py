def solution(n, lost, reserve):
    inter_num = set(reserve).intersection(lost)
    lost = list(set(lost) - inter_num)
    reserve = list(set(reserve) - inter_num)
    cnt = len([i for i in range(1, n+1) if i not in lost])
    for i in range(1, n+1):
        if i in lost:
            for idx, r in enumerate(reserve):
                if abs(i-r) == 1:
                    cnt += 1
                    lost.pop(lost.index(i))
                    reserve.pop(idx)
                    print(lost, reserve)
                    break
    return cnt