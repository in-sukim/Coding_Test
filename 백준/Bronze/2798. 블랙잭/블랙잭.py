n,m = map(int, input().split())

cards = list(map(int, input().split()))


max_num = 0
for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      sum_num =  cards[i] + cards[j] + cards[k]
      if sum_num <= m:
        if max_num < sum_num:
          max_num = sum_num
print(max_num)