def solution(s):
    chr_list = []
    answer = []
    for idx, i in enumerate(s):
        if i not in chr_list:
            answer.append(-1)
        else:
            exists_idx = 0
            for chr_idx, chr in enumerate(chr_list):
                if i == chr:
                    exists_idx = chr_idx
            answer.append(idx - exists_idx)
            
        chr_list.append(i)
    return answer