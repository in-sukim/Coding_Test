def solution(s):
    return int(s) if s[0] != '-' else int(s[1:]) - 2 * int(s[1:])