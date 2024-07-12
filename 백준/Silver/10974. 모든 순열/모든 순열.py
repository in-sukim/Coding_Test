import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
n_array = [i for i in range(1, n+1)]

for i in list(permutations(n_array, n)):
  print(*i)