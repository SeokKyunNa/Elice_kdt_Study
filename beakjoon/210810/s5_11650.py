'''
좌표 정렬하기
'''
import sys
input = sys.stdin.readline

N = int(input())
coordinate = {}

for _ in range(N):
    x, y = map(int, input().split())
    if x in coordinate:
        coordinate[x].append(y)
    else:
        coordinate[x] = [y]

# print(coordinate)
for i in range(-100_000, 100_001):
    if i in coordinate:
        coordinate[i].sort()
        for j in coordinate[i]:
            print(i, j) 
