import sys
input = sys.stdin.readline
number = list(input())
number.sort(reverse = True)
print(''.join(number))