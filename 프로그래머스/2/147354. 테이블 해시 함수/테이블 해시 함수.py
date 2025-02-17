def solution(data, col, row_begin, row_end):
    data = sorted(data, key = lambda x: (x[col-1], -x[0]))
    
    result = 0
    for i in range(row_begin, row_end + 1):
        s_i = sum(value % i for value in data[i-1])
        result ^= s_i
    return result