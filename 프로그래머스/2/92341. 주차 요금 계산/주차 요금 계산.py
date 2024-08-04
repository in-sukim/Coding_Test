from collections import defaultdict
import math
def solution(fees, records):
    re_dic = defaultdict()
    re_fee = defaultdict(int)
    records = list(map(lambda x: x.split(' '), records))
    for record in records:
        hour, minute = map(int, record[0].split(':'))
        time = (hour * 60) + minute
        car_num = record[1]
        state = record[2]
        if car_num in re_dic:
            if re_dic[car_num][1] == 'IN':
                re_fee[car_num] += (time - re_dic[car_num][0])
        re_dic[car_num] = [time, state]
    for key, values in re_dic.items():
        if values[1] == 'IN':
            close_time = (23 * 60) + 59
            re_fee[key] += close_time - re_dic[key][0]
            
    re_fee = sorted(re_fee.items(), key = lambda x:x[0])
    result = []
    for car_num, cum_time in re_fee:
        if cum_time <= fees[0]:
            result.append(fees[1])
        else:
            cal_fee = fees[1] + (math.ceil(((cum_time - fees[0]) / fees[2])) * fees[3])
            result.append(cal_fee)
    return result