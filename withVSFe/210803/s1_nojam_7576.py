'''
Silver1 - 토마토 (#7576)
'''
# 익은 토마토가 점점 퍼지는 형태이므로, BFS를 사용하여야 한다.
from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            dq.apppend((i, j))

answer = 0  # 최소 날짜

# 안 익은 토마토가 아직도 있는지 확인하는 함수
def check(graph, N, M):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return False
    
    return True

while dq and not(check(graph, N, M)):
    answer += 1
    cnt = len(dq)   # 익은 토마토 개수
    for i in range(cnt):   # 익은 토마토만큼 반복
        x, y = dq.popleft()
        for idx in range(4):
            X = x + dx[idx]
            Y = y + dx[idx]

            if X < 0 or X >= N or Y < 0 or Y >= M:
                continue

            if graph[X][Y] == 0:
                graph[X][Y] = 1
                dq.append((X, Y))

if check(graph, N, M):
    print(answer)
else:
    print(-1)