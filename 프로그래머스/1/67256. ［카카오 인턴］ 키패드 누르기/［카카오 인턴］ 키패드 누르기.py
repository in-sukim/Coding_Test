def get_position(number):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    return keypad[number]

def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def solution(numbers, hand):
    # 초기 위치 설정
    left_pos = '*'
    right_pos = '#'
    result = ''
    
    for number in numbers:
        if number in [1, 4, 7]:
            result += 'L'
            left_pos = number
        elif number in [3, 6, 9]:
            result += 'R'
            right_pos = number
        else:
            left_dist = get_distance(get_position(left_pos), get_position(number))
            right_dist = get_distance(get_position(right_pos), get_position(number))
            
            if left_dist == right_dist:
                if hand == "right":
                    result += 'R'
                    right_pos = number
                else:
                    result += 'L'
                    left_pos = number
            elif left_dist < right_dist:
                result += 'L'
                left_pos = number
            else:
                result += 'R'
                right_pos = number
                
    return result