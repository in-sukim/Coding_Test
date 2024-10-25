def solution(answers):
    people = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
             ]
    
    cnt = [0] * len(people)
    
    for idx_a,i in enumerate(answers):
        for idx_p, j in enumerate(people):
            if i == j[idx_a % len(j)]:
                print(j[idx_a % len(j)])
                cnt[idx_p] += 1
    return [i + 1 for i ,v in enumerate(cnt) if v ==  max(cnt)]