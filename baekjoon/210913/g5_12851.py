'''
숨바꼭질2
범위 : 0 ~ (N,K) ~ 100,000
'''
from collections import deque

def hide_and_seek(N, K):
    visited = [-1 for n in range(100_001)]
    count = [0 for n in range(100_001)]
    dq = deque()
    min_sec = 0

    # 시작 좌표
    visited[N] = 0
    dq.append(N)
    while dq:
        # 현재 출발 좌표
        current = dq.popleft()

        # 다음 좌표가 동생의 좌표라면
        # 최초(가장 짧은 시간)방문이라면 min_sec를 저장하고 count 증가
        # 가장 짧은 시간 방문과 동일한 시간에 방문했다면 count 증가
        # if current+1==K or current-1==K or current*2==K:
        #     if min_sec == 0:
        #         min_sec = visited[current]+1
        #         count += 1
        #     else:
        #         if visited[current]+1 == min_sec:
        #             count += 1

        # 다음 좌표가 범위 안에 있고, 방문하지 않은 좌표라면
        # dq에 다음 좌표를 넣어주고
        # visited[다음좌표]에 visited[현재좌표]의 값보다 1 증가한 값을 넣어줌
        # visited의 값은 몇 번째 이동인지 알 수 있게해줌
        if current+1 <= 100_000:
            # 첫 방문
            if visited[current+1] == -1:
                dq.append(current+1)
                visited[current+1] = visited[current]+1
                count[current+1] += 1
            # 두 번 이상 방문
            else:
                # 이전에 방문했을 때의 횟수와 같다면(최소값이라면)
                if visited[current+1] == visited[current]+1:
                    dq.append(current+1)
                    count[current+1] += 1
        if current-1 >= 0:
            # 첫 방문
            if visited[current-1] == -1:
                dq.append(current-1)
                visited[current-1] = visited[current]+1
                count[current-1] += 1
            # 두 번 이상 방문
            else:
                # 이전에 방문했을 때의 횟수와 같다면(최소값이라면)
                if visited[current-1] == visited[current]+1:
                    dq.append(current-1)
                    count[current-1] += 1
        if current*2 <= 100_000:
            # 첫 방문
            if visited[current*2] == -1:
                dq.append(current*2)
                visited[current*2] = visited[current]+1
                count[current*2] += 1
            # 두 번 이상 방문
            else:
                # 이전에 방문했을 때의 횟수와 같다면(최소값이라면)
                if visited[current*2] == visited[current]+1:
                    dq.append(current*2)
                    count[current*2] += 1

    return [visited[K], count[K]]

N, K = map(int, input().split())

if N == K:
    result = [0, 1]
elif N > K:
    result = [N-K, 1]
else:
    result = hide_and_seek(N, K)

print(str(result[0]) + '\n' + str(result[1]))