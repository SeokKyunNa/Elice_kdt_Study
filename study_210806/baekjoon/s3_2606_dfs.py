'''
바이러스
'''
import sys

input = sys.stdin.readline

# N=컴퓨터(정점)의 수, M=연결된 컴퓨터 쌍(간선)의 수
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(1, M+1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0 for _ in range(N+1)]

# dfs는 재귀함수 사용
def dfs(V):
    visited[V] = 1
    for next in graph[V]:
        if visited[next] == 0:
            visited[next] = 1
            dfs(next)

dfs(1)
print(sum(visited)-1)