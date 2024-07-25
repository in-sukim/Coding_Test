import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(phone_book):
    phone_dic = defaultdict(int)
    for phone in phone_book:
        phone_dic[phone] = 1

    for phone in phone_book:
        temp = ''
        for num in phone:
            temp += num
            if (temp in phone_dic) and (temp != phone):
                return False
    return True