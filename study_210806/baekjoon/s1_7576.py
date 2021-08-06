'''
토마토
'''
import sys
from collections import deque

input = sys.stdin.readline

# M은 가로, N은 세로
M, N = map(int, input().split())
box = [[] for _ in range(N)]
for i in range(N):
    box[i] = list(map(int, input().split()))

dq = deque()

# 익은 토마토의 좌표
for n in range(N):
    for m in range(M):
        if box[n][m] == 1:
            dq.append([n, m])

print(dq)