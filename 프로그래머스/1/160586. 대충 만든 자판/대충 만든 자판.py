def solution(keymap, targets):
    result = []
    for target in targets:
        cnt = 0
        for t in target:
            flag = False
            min_value = 1000000000
            for i in range(len(keymap)):
                if t in keymap[i]:
                    flag = True
                    min_value = min(min_value, keymap[i].index(t))
            if not flag:
                cnt = -1
                break
            cnt += min_value + 1
        result.append(cnt)
    return result