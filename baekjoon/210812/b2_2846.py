'''
오르막길
'''
import sys
input = sys.stdin.readline

N = int(input())

road = list(map(int, input().split()))

maximum = 0
sum = 0

for i in range(1, N):
    if road[i] - road[i-1] > 0:
        sum += (road[i] - road[i-1])
    else:
        sum = 0
    maximum = max(maximum, sum)

print(maximum)