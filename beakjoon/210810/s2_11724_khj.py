'''
연결 요소의 개수
'''
# import sys
# sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [-1] + [0 for _ in range(n)]

def dfs(v):
    visited[v] = 1
    for next in graph[v]:
        if visited[next] == 0:
            dfs(next)

cnt = 0

while 0 in visited:
    v = visited.index(0)
    print(v)
    dfs(v)
    cnt += 1

print(cnt)