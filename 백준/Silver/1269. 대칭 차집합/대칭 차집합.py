import sys
input = sys.stdin.readline

a_n, b_n = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = len(list(set(a).difference(b))) + len(list(set(b).difference(a)))
print(answer)