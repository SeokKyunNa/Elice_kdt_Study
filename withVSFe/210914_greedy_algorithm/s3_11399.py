'''
ATM
'''
import sys
input = sys.stdin.readline

N = int(input())

P = list(map(int, input().split()))
P.sort()
result = 0
accum = 0
for num in P:
    accum += num
    result += accum

print(result)
