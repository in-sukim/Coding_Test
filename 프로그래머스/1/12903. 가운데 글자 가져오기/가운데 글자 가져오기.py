def solution(s):
    l = len(s)
    mid_idx = l//2
    if l % 2:
        return s[mid_idx]
    else:
        return s[mid_idx - 1: mid_idx+1]