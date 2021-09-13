'''
유기농 배추
'''
import sys
from collections import deque
input = sys.stdin.readline

def find_cabbage(graph):
    # 해당 좌표의 4방향을 체크할 리스트
    dn = [0, 0, -1, 1]
    dm = [-1, 1, 0, 0]
    count = 0

    dq = deque()
    # 전체 좌표를 검사
    for i in range(N):
        for j in range(M):
            # 배추가 심어져 있는 자리라면 그래프 탐색 수행
            if graph[i][j] == 1:
                count += 1
                dq.append([i, j])

                # BFS
                while dq:
                    n, m = dq.popleft()
                    # 배추가 심어져 있지 않으면 통과
                    if graph[n][m] == 0:
                        continue
                    # 배추가 심어져있다면 1을 더해서 1이 아닌 숫자로 만듦(방문 처리)
                    elif graph[n][m] == 1:
                        graph[n][m] += 1

                        # 해당 좌표의 4방향을 확인해서 배추가 심어져있다면 덱에 넣음
                        for d in range(4):
                            new_n = n + dn[d]
                            new_m = m + dm[d]
                            # 좌표 범위를 벗어나면 통과
                            if new_m < 0 or new_m > M-1 or new_n < 0 or new_n > N-1:
                                continue
                            # 배추가 심어져 있지 않거나(0) 이미 방문했다면(2) 통과
                            if graph[new_n][new_m] != 1:
                                continue

                            elif graph[new_n][new_m] == 1:
                                dq.append([new_n, new_m])

    return count


# T번 만큼 수행
T = int(input())
for _ in range(T):
    # M 가로길이, N 세로길이, K 배추 위치
    M, N, K = map(int, input().split())

    # 전체가 0으로 된 M * N 크기의 2차원 리스트 생성
    graph = [[0 for _ in range(M)] for _ in range(N)]
    # 배추 위치 입력
    for _ in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1

    print(find_cabbage(graph))


