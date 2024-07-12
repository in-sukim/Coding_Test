import sys
input = sys.stdin.readline

words = input().strip()
find_word = input().strip()

i = 0
cnt = 0
while i < len(words):
  a = i+len(find_word)
  if words[i:i+len(find_word)] == find_word:
    i += len(find_word)
    cnt += 1
  else:
    i += 1
print(cnt)