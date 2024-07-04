import sys
input = sys.stdin.readline

n,m = map(int,input().split())
rice_cakes = list(map(int,input().split()))

rice_cakes.sort()
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  cut_rice_cakes = [i-array[mid] if i >= array[mid] else 0 for i in array ]
  if sum(cut_rice_cakes) == target:
    return mid
  elif sum(cut_rice_cakes) >  target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

print(binary_search(rice_cakes, m, 0, n-1))
