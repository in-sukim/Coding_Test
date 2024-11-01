import re 
def solution(new_id):
    possible_pattern = re.compile('[a-z0-9\-\_\.]')
    
    step1 = new_id.lower()
    step2 = ''.join(possible_pattern.findall(step1))
    step3 = re.sub(r'\.+', '.', step2)

    if step3.startswith('.'):
        step3 = step3[1:]
    if step3.endswith('.'):
        step3 = step3[:-1]
    if not len(step3):
        step3 = 'a'

    if len(step3) >= 16:
        step3 = step3[:-len(step3)+15]
        if step3.endswith('.'):
            step3 = step3[:-1]

    if len(step3) <= 2:
        iter_num = 3 - len(step3)
        step3 += step3[-1] * iter_num
    return step3