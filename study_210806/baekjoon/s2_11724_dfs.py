'''
연결 요소의 개수
'''
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# N은 정점의 개수, M은 간선의 개수
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
# 두 개의 정점을 입력 받아 간선의 개수만큼 반복하여 그래프를 인접 리스트로 만듦
for _ in range(1, M+1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 방문을 확인할 리스트
visited = [0 for _ in range(N+1)]
# 연결 요소의 개수를 정할 변수
visit_num = 1

# DFS 구현
def DFS(v):
    visited[v] = visit_num
    for next in graph[v]:
        if visited[next] == 0:
            visited[next] = visit_num
            DFS(next)


# 전체 정점을 돌면서 방문하지 않은 곳이 있다면 dfs로 방문
# 하나의 연결 요소가 끝나면 visit_num을 1 추가
# visited 리스트는 첫 번째 연결 요소는 1로, 두 번째 연결 요소는 2로, ... 채워짐
for vertex in range(1, N+1):
    if visited[vertex] == 0:
        DFS(vertex)
        visit_num += 1
        
# visited 리스트에서 최대값(몇 번째 연결 요소인지) 출력
print(max(visited))