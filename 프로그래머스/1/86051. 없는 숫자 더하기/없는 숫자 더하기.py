def solution(numbers):
    ground_truth = sum([i for i in range(10)])
    return ground_truth - sum(numbers)