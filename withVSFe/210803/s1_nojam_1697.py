'''
Silver1 - 숨바꼭질 (#1697)
'''
from collections import deque

N, K = map(int, input())

visited = [-1] * 200000
dq = deque()

dq.append(N)
visited[N] = 0

while dq:
    x = dq.popleft()

    # 현재 노드 -1인 지점
    # visited의 값이 -1이면 아직 방문하지 않은 노드
    if 0 <= x - 1 <= 200000 and visited[x - 1] == -1:
        visited[x - 1] = visited[x] + 1
        dq.append(x - 1)

    # 현재 노드 +1인 지점
    if 0 <= x + 1 <= 200000 and visited[x + 1] == -1:
        visited[x + 1] = visited[x] + 1
        dq.append(x + 1)

    # 현재 노드 *2인 지점
    if 0 <= x * 2 <= 200000 and visited[x * 2] == -1:
        visited[x * 2] = visited[x] + 1
        dq.append(x * 2)


print(visited[K])