import math
def solution(arrayA, arrayB):
    a = arrayA[0]
    b = arrayB[0]
    
    for i in range(len(arrayA)):
        a = math.gcd(a, arrayA[i])
        b = math.gcd(b, arrayB[i])
    
    cul = 1
    young = 1
    
    for i in range(len(arrayA)):
        if arrayB[i] % a == 0:
            cul = 0
        if arrayA[i] % b == 0:
            young = 0
    if cul == 0 and young == 0:
        return cul
    else:
        return max(a,b)