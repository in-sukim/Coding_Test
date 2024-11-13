import re  
def solution(files):
    new = list(
        map(
            lambda x: re.split('(\d{1,5})', x.lower()), files
        )
    )
    new = [i[:-1]+[idx] for idx,i in enumerate(new)]
    new.sort(key = lambda x: (x[0], int(x[1]), x[-1]))
    result = [files[i[-1]] for i in new]
    return result
    