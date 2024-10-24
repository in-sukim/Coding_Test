from itertools import combinations
def solution(nums):
    pick_num = len(nums)//2
    nums = list(set(nums))
    if len(nums) < pick_num:
        return len(nums)
    return pick_num