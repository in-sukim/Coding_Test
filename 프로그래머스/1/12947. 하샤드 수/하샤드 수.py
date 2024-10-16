def solution(x):
    div_n = 0
    for i in str(x):
        div_n += int(i)
    return False if x % div_n else True