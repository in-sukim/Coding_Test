import sys
input = sys.stdin.readline

n, k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()

start = 0
end = -1
result = []
before_value = 0

while len(result) < k:
  if len(result) % 2:
    pop_value = data[start]
    before_value = pop_value
    start += 1
    result.append(0)
  else:
    pop_value = data[end]
    end -= 1
    diff = pop_value - before_value
    result.append(diff)

print(sum(result))
