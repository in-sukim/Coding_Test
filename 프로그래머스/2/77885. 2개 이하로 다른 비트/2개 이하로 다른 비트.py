def num2binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        n, remain = divmod(n,2)
        binary = str(remain) + binary
    return binary
    
    
def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            binary = '0' + num2binary(num)
            right_idx = binary.rfind('0')
            binary = list(binary)
            
            binary[right_idx] = '1'
            binary[right_idx+1] = '0'
            
            binary = ''.join(binary)
            binary2num = int(binary, 2)
            answer.append(binary2num)
    return answer