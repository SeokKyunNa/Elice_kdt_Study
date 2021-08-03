'''
Silver1 - 단지 번호 붙이기 (#2667)
'''
N = int(input())

graph = [input() for i in range(N)]

cnt = []
visited = [[0] * N for i in range(N)]

# 좌표 이동값 설정
# 위쪽   : (x-1, y)
# 아랫쪽 : (x+1, y)
# 왼쪽   : (x, y-1)
# 오른쪽 : (x+1, y)
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, 1]

# 깊이 우선 탐색
def dfs(x, y, number):
    visited[x][y] = number

    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X < 0 or X >= N or Y < 0 or Y >= N:
            continue
        if not(visited[X][Y]) and graph[X][Y] == '1':
            dfs(X, Y, number)
    

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not(visited[i][j]):
            dfs(i, j, len(cnt) + 1)
            # len(cnt) = 0 -> 1을 채워넣고
            # 1의 갯수를 세서 cnt 배열에 넣음
            # 그럼 이제 len(cnt) + 1 = 2

            count = visited[i].count(len(cnt) + 1)
            cnt.append(count)

print(len(cnt))
print(*sorted(cnt), sep='\n')
