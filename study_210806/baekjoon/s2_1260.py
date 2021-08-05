'''
DFS와 BFS
'''
import sys
from collections import deque

input = sys.stdin.readline

# 정점의 개수 N, 간선의 개수 M, 시작 정점 V
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

bfs_result = []
dfs_result = []
bfs_visited = [0 for _ in range(N+1)]
dfs_visited = [0 for _ in range(N+1)]

for i in range(1, M+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()

def DFS(V):
    dfs_visited[V] = 1
    dfs_result.append(V)
    for next in graph[V]:
        if dfs_visited[next] == 0:
            DFS(next)

def BFS(V):
    dq = deque()
    dq.append(V)
    bfs_visited[V] = 1
    bfs_result.append(V)
    while dq:
        x = dq.popleft()
        for next in graph[x]:
            if bfs_visited[next] == 0:
                bfs_visited[next] = 1
                bfs_result.append(next)
                dq.append(next)
            
DFS(V)
BFS(V)

print(*dfs_result)
print(*bfs_result)