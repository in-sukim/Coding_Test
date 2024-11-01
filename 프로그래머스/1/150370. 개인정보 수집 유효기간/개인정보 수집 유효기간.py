from dateutil.relativedelta import relativedelta
from datetime import datetime
from collections import defaultdict

def to_days(date):
    y, m, d = map(int, date.split('.'))
    return y*12*28 + m*28 + d

def solution(today, terms, privacies):
    alpha_dic = defaultdict(int)
    today = to_days(today)
    privacies = [i.split(' ') for i in privacies]
    
    for t in terms:
        key, value = t.split(' ')
        alpha_dic[key] = int(value) * 28
    result = []
    for idx, (pri_date, alpha) in enumerate(privacies):
        term = alpha_dic[alpha]
        pri_date = to_days(pri_date)
        
        if pri_date + term - 1 < today:
            result.append(idx + 1)
    return result
        