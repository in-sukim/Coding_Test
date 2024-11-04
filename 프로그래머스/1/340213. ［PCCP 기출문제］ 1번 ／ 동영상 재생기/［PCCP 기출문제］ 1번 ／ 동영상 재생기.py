def t2s(time):
    m,s = map(int, time.split(':'))
    return m * 60 + s

def s2t(seconds):
    m , s = divmod(seconds, 60)
    return str(m).zfill(2) + ':' + str(s).zfill(2)

def solution(video_len, pos, op_start, op_end, commands):
    video_len = t2s(video_len)
    pos = t2s(pos)
    op_start = t2s(op_start)
    op_end = t2s(op_end)
    
    for comm in commands:
        if comm == 'next':
            if op_start <= pos <= op_end:
                pos = op_end
            pos += 10
            if pos > video_len:
                pos = video_len
        if comm == 'prev':
            if op_start <= pos <= op_end:
                pos = op_end
            pos -= 10
            if pos < 0:
                pos = 0
        if op_start <= pos <= op_end:
            pos = op_end
        print(s2t(pos), pos)
    return s2t(pos)