def solution(data, ext, val_ext, sort_by):
    index_dic = {
        'code' : 0,
        'date' : 1,
        'maximum' : 2,
        'remain' : 3
        
    }

    new_data = []
    for idx, i in enumerate(data):
        compare_value = i[index_dic[ext]]
        if compare_value < val_ext:
            new_data.append(data[idx])
    new_data.sort(key = lambda x: x[index_dic[sort_by]])
    return new_data
    