def solution(prices):
    result = []
    for idx, value in enumerate(prices):
        standard_value = prices[idx]
        compare_idx = idx + 1
        while compare_idx < len(prices):
            if standard_value > prices[compare_idx]:
                compare_idx += 1
                break
            compare_idx += 1
        result.append(compare_idx - (idx+1))
    return result
