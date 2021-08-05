'''
DFS와 BFS
'''
import sys
from collections import deque

input = sys.stdin.readline

# N=정점의 개수, M=간선의 개수, V=시작 정점
N, M, V = map(int, input().split())

# 그래프 입력
graph = [[] for _ in range(N+1)]
# 간선의 개수만큼 입력 받음
# 양방향 그래프이므로 양쪽 정점에 서로를 넣어줌
for _ in range(1, M+1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# 조건에 따라 정점 번호가 작은 것 부터 방문해야 하므로 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

# 방문 여부를 확인할 리스트
dfs_visited = [0 for _ in range(N+1)]
bfs_visited = [0 for _ in range(N+1)]
# 방문한 순서대로 넣어줄 결과 리스트
dfs_result = []
bfs_result = []

# 재귀함수를 사용
def DFS(V):
    dfs_visited[V] = 1  # 방문 처리
    dfs_result.append(V)    # 결과 리스트에 넣어줌
    # 한 정점의 인접 정점을 돌면서 재귀
    for next in graph[V]:
        if dfs_visited[next] == 0:  # 방문하지 않았다면
            dfs_visited[next] = 1   # 방문 처리
            DFS(next)   # 재귀

# deque을 사용
def BFS(V):
    dq = deque()
    dq.append(V)    # 시작 정점을 덱에 넣어줌
    bfs_visited[V] = 1  # 시작 정점 방문 처리
    bfs_result.append(V)    # 시작 정점을 결과 리스트에 넣어줌

    while dq:   # 덱에 값이 있는 동안 실행
        x = dq.popleft()    # 덱의 맨 처음 값을 꺼냄

        # 현재 정점의 인점 정점들을 돌면서 실행
        for next in graph[x]:
            if bfs_visited[next] == 0:  # 방문하지 않았다면
                bfs_visited[next] = 1   # 방문 처리
                bfs_result.append(next) # 결과 리스트에 넣어줌
                dq.append(next) # 덱에 인접 정점을 넣어줌

# 함수 실행
DFS(V)
BFS(V)
# 결과 리스트 언패킹해서 출력
print(*dfs_result)
print(*bfs_result)