'''
수 정렬하기2
'''
import sys
input = sys.stdin.readline

N = int(input())
set_num = set()

for _ in range(N):
    number = int(input())
    set_num.add(number)

for i in range(-1_000_000, 1_000_001):
    if i in set_num:
        print(i)