import heapq
import sys
input = sys.stdin.readline
n = int(input())
cards = []
for i in range(n):
  heapq.heappush(cards, int(input()))

total = 0

while len(cards) > 1:
  card1 = heapq.heappop(cards)
  card2 = heapq.heappop(cards)
  # print(card1, card2)

  sum_card = card1 + card2
  total += sum_card
  heapq.heappush(cards, sum_card)
print(total)