def solution(n):
    find_one = format(n, 'b').count('1')
    cnt_one = 0

    while True:
        n += 1
        cur_binary = format(n, 'b')
        cnt_one = cur_binary.count('1')
        if cnt_one == find_one:
            return n