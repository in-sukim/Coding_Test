from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)
        most_ordered = Counter(order_combinations).most_common()
    
        if len(most_ordered) == 0:
            continue
        max_value = most_ordered[0][1]
        
        for key, value in most_ordered:
            if value > 1 and value == max_value:
                answer.append(''.join(key))

    return sorted(answer)
