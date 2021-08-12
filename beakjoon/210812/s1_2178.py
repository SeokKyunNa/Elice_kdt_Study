'''
미로 탐색
'''
import sys
from collections import deque
input = sys.stdin.readline

# 미로 입력
N, M = map(int, input().split())
maze = [[] for n in range(N)]
for i in range(N):
    for j in input().rstrip():
        maze[i].append(int(j))

# 초기값
count = 2
dm = [-1, 1, 0, 0]
dn = [0, 0, -1, 1]
dq = deque()
dq.append([0, 0])

# 덱에 값이 1인(방문해야할) 좌표들을 담고
# 인접해있는 1 좌표들을 현재 좌표의 값에 1을 더한 값으로 치환
# 첫번째 칸은 1, 거기서 갈 수 있는 좌표들은 2, 그 다음으로 갈 수 있는 좌표들은 3...
# 술래잡기 문제에서 힌트 얻음 
# (1번 점프해서 갈 수 있는 곳들은 전부 1, 2번 점프해서 갈 수 있는 곳들은 전부 2...)
while dq:
    # 덱의 첫 번째 값을 꺼냄
    n, m = dq.popleft()
    # count는 다음 방문했을 때 치환해줄 값이므로 현재 좌표의 값+1
    count = maze[n][m]+1

    # 현재 좌표에서 상하좌우 4방향 좌표를 확인
    for d in range(4):
        new_n = n + dn[d]
        new_m = m + dm[d]
        # 좌표를 벗어나거나, 시작 좌표(0, 0)은 통과
        if new_n < 0 or new_m < 0 or new_n > N-1 or new_m > M-1 or (new_n == 0 and new_m == 0):
            continue
        # 1이 아니라면 이미 방문했거나 0이므로 통과
        if maze[new_n][new_m] != 1:
            continue
        # 방문해야할 좌표의ㅣ 값을 count로 바꾸고 덱에 넣음
        maze[new_n][new_m] = count
        dq.append([new_n, new_m])
        
# 출력 조건이 N, M에 도달하는 최소경로이므로
# 위에서 최소 경로로 도착한 N, M 좌표의 값을 출력해줌
# 리스트는 0, 0부터 시작이므로 1씩 빼줌
print(maze[N-1][M-1])