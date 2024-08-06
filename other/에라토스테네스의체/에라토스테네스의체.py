# def solution(num):
#   result = []
#   all = [i for i in range(2, num+1)]
#   for i in range(len(all)):
#     standard_value = all[i]
#     if all[i] == 0:
#       continue
#     else:
#       while i + standard_value < len(all):
#         all[i+standard_value] = 0
#         i += standard_value
#   result = [i for i in all if i!= 0]
#   print(result)    

import math

def solution(num):
  array = [True for i in range(num+1)]
  for i in range(2, int(math.sqrt(num)) + 1):
    if array[i] == True:
      j = 2
      while i * j <= num:
        array[i * j] = False
        j += 1
        
  result = []
  for i in range(2, num+1):
    if array[i]:
      result.append(i)
  return result
num = 26
print(solution(num))
