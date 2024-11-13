def solution(files):
    new_files = []
    for f_idx, file in enumerate(files):
        before = file[0].isdecimal()
        standard = []
        num_start = -1
        for idx, i in enumerate(file):
            current = i.isdecimal()
            if current != before:
                standard.append(idx)
                if current:
                    num_start = idx
            before = current
            
            if num_start != -1 and current and idx - num_start >= 5:
                if len(standard) % 2 == 1:
                    standard.append(idx)
                    break
        if not standard:
            continue
            
        head = file[:standard[0]].lower()
        number_end = min(standard[0] + 5, standard[1] if len(standard) > 1 else len(file))
        number = int(file[standard[0]:number_end])
        new_files.append([head, number, f_idx])
    new_files.sort(key = lambda x: (x[0], x[1], x[2]))
    result = [files[i[-1]] for i in new_files]
    return result