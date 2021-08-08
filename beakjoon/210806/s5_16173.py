'''
점프왕 쩰리(Small)
'''
import sys
from collections import deque
input = sys.stdin.readline

# 지도 크기를 입력받고 2차원 리스트로 만듦
N = int(input())
_list = [[] for _ in range(N)]
# 데이터 입력
for i in range(N):
    _list[i] = list(map(int, input().split()))
# 방문 여부를 확인할 리스트 (단방향이지만, 시간초과 문제로 인해 필요함)
visited = [[0 for _ in range(N)] for _ in range(N)]

def haruhing():
    dq = deque()
    dq.append([0, 0])   # 시작점은 왼쪽 위 최끝단
    while dq:
        x, y = dq.popleft()
        if x > N-1 or y > N-1:  # 지도를 벗어난 좌표는 연산하지 않음
            continue
        elif x == N-1 and y == N-1: # 끝점인 오른쪽 아래 최끝단에 도착
            print("HaruHaru")
            exit()
        else:
            if visited[x][y] == 0:  # 방문하지 않았다면
                visited[x][y] = 1
                new_x = x + _list[x][y] # 새로운 x좌표 생성
                new_y = y + _list[x][y] # 새로운 y좌표 생성
                dq.append([x, new_y])   # 새로운 y좌표로 이동한 좌표를 dq에 넣어줌
                dq.append([new_x, y])   # 새로운 x좌표로 이동한 좌표를 dq에 넣어줌
    
    print("Hing")

haruhing()