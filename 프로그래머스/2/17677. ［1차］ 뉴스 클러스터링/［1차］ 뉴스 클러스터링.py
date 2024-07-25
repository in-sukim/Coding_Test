import sys
from collections import Counter
import re
def solution(str1, str2):
    str1_list = list()
    str2_list = list()
    for i in range(len(str1)):
        value = re.sub('[^A-Z]', '', str1[i: i+2].upper())
        if len(value) == 2:
            str1_list.append(value.upper())

    for i in range(len(str2)):
        value = re.sub('[^A-Z]', '', str2[i: i+2].upper())
        if len(value) == 2:
            str2_list.append(value.upper())

    if len(str1_list) == 0 and len(str2_list) == 0:
        return 65536

    if len(set(str1_list)) == 1 and len(set(str2_list)) == 1:
        if str1_list[0] == str2_list[0]:
            len_str1 = len(str1_list) 
            len_str2 = len(str2_list)
            num = min(len_str1, len_str2)
            denum = max(len_str1, len_str2)
            return int((num / denum) * 65536)

    counter_1 = Counter(str1_list)
    counter_2 = Counter(str2_list)

    union_value = set((counter_1+counter_2).elements())
    inter_value = set((counter_1&counter_2).elements())

    num = 0
    for inter in inter_value:
        min_union = min(counter_1[inter], counter_2[inter])
        num += min_union

    denum = 0
    for union in union_value:
        max_union = max(counter_1[union], counter_2[union])
        denum += max_union
    return int((num / denum) * 65536)