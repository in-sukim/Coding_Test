from collections import defaultdict
def solution(record):
    record_dic = defaultdict(int)
    for r  in record:
        split_r = r.split(' ')
        if len(split_r) == 3:
            record_dic[split_r[1]] = [split_r[0], split_r[2]]
        else:
            record_dic[split_r[1]][0] = split_r[0]
    # print(record_dic)
    result = []
    for r in record:
        split_r = r.split(' ')
        current_nick = record_dic[split_r[1]][1]
        if split_r[0] == 'Enter':
            print_value = f"{current_nick}님이 들어왔습니다."
            result.append(print_value)
        elif split_r[0] == 'Leave':
            print_value = f"{current_nick}님이 나갔습니다."
            result.append(print_value)
    return result