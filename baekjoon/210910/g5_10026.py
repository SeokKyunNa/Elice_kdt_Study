'''
적록색약
일반, 적록색약 각각 나눠서 함수 작성
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
grid = [] * N

for i in range(N):
    grid.append(input().rstrip())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dq = deque()

# 일반인 검사 함수
def normal(graph):
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 전체 좌표를 탐색
    for i in range(N):
        for j in range(N):
            # 방문하지 않은 곳 방문
            if visited[i][j] == 0:
                count += 1
                
                # 주변 탐색
                dq.append([i, j])
                while dq:
                    n, m = dq.popleft()
                    visited[n][m] = count
                    
                    # 4방향(상하좌우)을 탐색
                    for d in range(4):
                        new_n = n + dx[d]
                        new_m = m + dy[d]

                        if [new_n, new_m] in dq:
                            continue

                        if new_m < 0 or new_m > N-1 or new_n < 0 or new_n > N-1:
                            continue
                        
                        if grid[new_n][new_m] != grid[n][m] or visited[new_n][new_m] != 0:
                            continue
                        else:
                            dq.append([new_n, new_m])

    return count

# 적록색약 검사 함수
def color_weakness(graph):
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 전체 좌표를 탐색
    for i in range(N):
        for j in range(N):
            # 방문하지 않은 곳 방문
            if visited[i][j] == 0:
                count += 1
                
                # 주변 탐색
                dq.append([i, j])
                while dq:
                    n, m = dq.popleft()
                    visited[n][m] = count
                    
                    # 4방향(상하좌우)을 탐색
                    for d in range(4):
                        new_n = n + dx[d]
                        new_m = m + dy[d]

                        if [new_n, new_m] in dq:
                            continue

                        if new_m < 0 or new_m > N-1 or new_n < 0 or new_n > N-1:
                            continue
                        
                        if grid[n][m] in ['R', 'G']:
                            if grid[new_n][new_m] == 'B' or visited[new_n][new_m] != 0:
                                continue
                            else:
                                dq.append([new_n, new_m])
                        else:
                            if grid[new_n][new_m] != grid[n][m] or visited[new_n][new_m] != 0:
                                continue
                            else:
                                dq.append([new_n, new_m])

    return count

print(normal(grid), color_weakness(grid))
