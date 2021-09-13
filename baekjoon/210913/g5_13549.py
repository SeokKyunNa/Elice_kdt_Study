'''
숨바꼭질3
범위 : 0 ~ (N,K) ~ 100,000
'''
from collections import deque

def hide_and_seek(N):
    visited = [-1 for n in range(100_001)]
    dq = deque()

    # 시작 좌표
    visited[N] = 0
    dq.append(N)
    while dq:
        # 현재 출발 좌표
        current = dq.popleft()

        # 다음 좌표가 동생의 좌표라면 return
        if current*2==K:
            return visited[current]
        if current+1==K or current-1==K:
            return visited[current]+1

        # 다음 좌표가 범위 안에 있고, 방문하지 않은 좌표라면
        # dq에 다음 좌표를 넣어주고
        # visited[다음좌표]에 visited[현재좌표]의 값보다 1 증가한 값을 넣어줌
        # visited의 값은 몇 번째 이동인지 알 수 있게해줌
        if current*2 <= 100_000 and visited[current*2] == -1:
            dq.appendleft(current*2)
            visited[current*2] = visited[current]
        if current+1 <= 100_000 and visited[current+1] == -1:
            dq.append(current+1)
            visited[current+1] = visited[current]+1
        if current-1 >= 0 and visited[current-1] == -1:
            dq.append(current-1)
            visited[current-1] = visited[current]+1

N, K = map(int, input().split())

if N == K:
    print(0)
elif N > K:
    print(N-K)
else:
    print(hide_and_seek(N))