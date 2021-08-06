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

# 거지 같은 케이스..
sum = 0
for i in range(N):
    for j in range(M):
        sum += box[i][j]
if sum == -(M*N):
    print(0)
    exit()


dq = deque()
# 익은 토마토의 좌표 (흠. 최대 1000*1000인데 시간 초과 안 걸릴려나)
for n in range(N):
    for m in range(M):
        if box[n][m] == 1:
            dq.append([n, m])
day = 0
while dq:
    # check = False
    for _ in range(len(dq)):
        x, y = dq.popleft()
        # 아랫쪽
        if x+1 > N-1 or box[x+1][y] != 0: pass
        else: box[x+1][y]=1; dq.append([x+1, y])
        # 윗쪽
        if x-1 < 0 or box[x-1][y] != 0: pass
        else: box[x-1][y]=1; dq.append([x-1, y])
        # 왼쪽
        if y-1 < 0 or box[x][y-1] != 0: pass
        else: box[x][y-1]=1; dq.append([x, y-1])
        # 오른쪽
        if y+1 > M-1 or box[x][y+1] != 0: pass
        else: box[x][y+1]=1; dq.append([x, y+1])
    day += 1

for i in range(N):
    if 0 in box[i]:
        print(-1)
        exit()

print(day-1)    # while dq를 돌면서 하루가 더 더해짐..
exit()


'''
토마토가 없을 때는 안 익은게 아니라 모두 익은 것으로 간주해야 함
거지 같은 케이스..
6 4
-1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1
'''