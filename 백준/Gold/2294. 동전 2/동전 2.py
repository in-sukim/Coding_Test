[n,k] = list(map(int,input().split())) # k=15

coin_set = []
for i in range(n):
    coin_set.append(int(input()))
coin_set = list(set(coin_set)) #1,5,12

cnt = [-1]*(k+1)
cnt[0] = 0 # cnt = [0,-1,-1,-1,...]
for i in range(1,k+1):
    if i>=min(coin_set):
        min_cnt = [] # coin_set의 각 동전 사용하는 경우
        for coin in coin_set:
            if i>=coin:
                min_cnt.append(cnt[i-coin]) 
        min_cnt = sorted(list(set(min_cnt)))
        if min_cnt[-1]==-1: # 모든 경우 -1
            continue
        elif min_cnt[0]==-1:
            cnt[i] = 1 + min_cnt[1] # -1/-1 아닌 경우 모두 존재
        else:
            cnt[i] = 1 + min_cnt[0]

print(cnt[-1])