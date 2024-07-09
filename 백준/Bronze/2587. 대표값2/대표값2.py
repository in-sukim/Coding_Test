import sys
input = sys.stdin.readline

numbers = [int(input()) for _ in range(5)]
numbers.sort()

everage = sum(numbers) / len(numbers)
mid = numbers[len(numbers) // 2]
print(int(everage))
print(mid)