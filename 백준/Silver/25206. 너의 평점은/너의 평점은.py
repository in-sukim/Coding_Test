alpha_list = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
alpha_dic = dict()
for alpha, score in zip(alpha_list, score_list):
  alpha_dic[alpha] = float(score)
  
total = 0
hak_total = 0
for _ in range(20):
  object, hak, alpha = input().split()
  if alpha != 'P':
    total += float(hak) * alpha_dic[alpha]
    hak_total += float(hak)
  else:
    pass
print(round(total / hak_total, 6))