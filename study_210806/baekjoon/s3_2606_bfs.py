'''
바이러스
'''
import sys
from collections import deque

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

# deque쓰는건 bfs
def bfs():
    visited[1] = 1
    dq = deque()
    dq.append(1)
    while dq:
        x = dq.popleft()
        for next in graph[x]:
            if visited[next] == 0:
                visited[next] = 1
                dq.append(next)

bfs()
print(sum(visited)-1)