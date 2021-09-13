'''
단지 번호 붙이기
'''
import sys
from collections import deque

iput = sys.stdin.readline

N = int(input())

complex = [input() for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

# 상하좌우 확인에 사용할 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dq = deque()
visit = 0   # 몇 번째 단지인지 체크할 변수
count = [0] # 해당단지에서 몇 번째 집을 방문했는지 체크할 변수 (0번째 단지는 0으로 시작)
# 전체 단지를 돌면서 확인
for i in range(N):
    for j in range(N):
        # 이미 방문했거나, 집이 없다면 continue
        if visited[i][j] > 0 or complex[i][j] == '0':
            continue
        # 집이 있는데 방문하지 않은 곳에 대한 연산
        dq.append([i, j])   # 시작할 집 좌표
        visit += 1  # 방문 체크 값을 1 늘려줌 (몇 번째 방문 단지인지)
        count.append(0) # 한 단지 안의 몇 번째 집인지 체크할 값을 만들어줌
        # BFS
        while dq:
            x, y = dq.popleft()
            if visited[x][y] > 0:
                continue
            visited[x][y] = visit
            # 방문한 단지별 count 계산
            count[visit] += 1
            # 상하좌우 좌표를 확인
            for d in range(4):
                new_x = x + dx[d]
                new_y = y + dy[d]
                # 0보다 작거나, 전체 단지 크기보다 큰 좌표는 넘김
                if new_x < 0 or new_y < 0 or new_x > N-1 or new_y > N-1:
                    continue
                else:
                    # 유효한 좌표값 중 방문하지 않았고, 집이 있는 곳은 dq에 넣어줌
                    if visited[new_x][new_y] == 0 and complex[new_x][new_y] == '1':
                        dq.append([new_x, new_y])

print(visit)    # 단지의 개수 출력
count.sort()    # 출력 조건을 만족하기 위해 오름차순 정렬
# 정렬된 단지 별 집의 개수를 출력
for i in range(1, len(count)):
    print(count[i])