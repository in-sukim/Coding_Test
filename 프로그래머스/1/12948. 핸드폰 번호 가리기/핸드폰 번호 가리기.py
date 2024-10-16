def solution(phone_number):
    front_l = len(phone_number) - 4
    return '*'* front_l + phone_number[-4:]