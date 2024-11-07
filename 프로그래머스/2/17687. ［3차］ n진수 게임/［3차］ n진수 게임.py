# number -> base 진수 변환
def convert_number(n, base):
    temp = "0123456789ABCDEF"
    q,r = divmod(n, base)
    
    if q == 0:
        return temp[r]
    else:
        return convert_number(q,base) + temp[r]
    
def solution(n,t,m,p):
    answer = ''
    
    num = 0
    while True:
        print(convert_number(num,n))
        answer += convert_number(num,n)
        
        if len(answer) >= t * m:
            answer = answer[:t*m]
            return answer[p-1: t*m:m]
        num += 1
    
