def count_move(current_num, target_num):
    # 키패드를 좌표로 매핑
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2),
        10: (3, 0), 11: (3, 1), 12: (3, 2)
    }
    
    current = keypad[current_num]
    target = keypad[target_num]
    
    return abs(current[0] - target[0]) + abs(current[1] - target[1])

def solution(numbers, hand):
    L_dic = {
        1 : 'L',
        4 : 'L',
        7 : 'L'
    }
    R_dic = {
        3 : 'R',
        6 : 'R',
        9 : 'R'
    }
    cal_list = [2,5,8,0]
    left, right = 10, 12
    result = ''
    for number in numbers:
        if number not in cal_list:
            if number in L_dic:
                value = L_dic[number]
                left = number
            else:
                value = R_dic[number]
                right = number
            result += value
        else:
            left_cnt = count_move(left, number)
            right_cnt = count_move(right, number)
            if left_cnt == right_cnt:
                result += hand[0].upper()
                if hand == 'right':
                    right = number
                else:
                    left = number
            elif left_cnt > right_cnt:
                result += 'R'
                right = number
            else:
                result += 'L'
                left = number
    return result