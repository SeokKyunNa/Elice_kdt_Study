'''
연결 요소의 개수
'''
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(N+1)]

dq = deque()
dq.append(1)
count = 0

for v in range(1, N+1):
    if visited[v] == 0: 
        dq.append(v)
        count += 1
        while dq:
            u = dq.popleft()
            if visited[u] == 0:
                visited[u] = count
                for node in graph[u]:
                    if visited[node] == 0:
                        dq.append(node)
                
print(max(visited))
