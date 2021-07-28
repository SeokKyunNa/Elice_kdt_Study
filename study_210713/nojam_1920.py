import sys
import random
import time

input = sys.stdin.readline()

a, b = map(int, input())

count = 0
_set = set(map(int, input().split()))
M = int(input())

# _list = list(map(int, input().split()))

# for dt in _list:
#     if dt in _set:
#         print(1)
#     else:
#         print(0)

print(*[1 if dt in _set else 0 for dt in map(int, input().split(), sep='\n')])
