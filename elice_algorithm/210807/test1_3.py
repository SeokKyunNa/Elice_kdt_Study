'''
공 굴리기
'''
import sys
from collections import deque

input = sys.stdin.readline

def main():
    # N줄 M칸
    N, M = map(int, input().split())
    direction = [[] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        direction[i] = list(map(int, input().split()))
    
    y, x = map(int, input().split())
    result = 0
    count = 0

    dq = deque()
    dq.append([y-1, x-1])

    while dq:
        y, x = dq.popleft()
        if visited[y][x] == 0:
            visited[y][x] = 1
            if direction[y][x] == 1:
                if y-1 < 0: break
                else: next_x = x; next_y = y-1
            elif direction[y][x] == 2:
                if x-1 < 0: break
                else: next_x = x-1; next_y = y
            elif direction[y][x] == 3:
                if x+1 > M-1: break
                else: next_x = x+1; next_y = y
            else:
                if y+1 > N-1: break
                else: next_x = x; next_y = y+1

            dq.append([next_y, next_x])
        elif visited[y][x] == 1:
            visited[y][x] = 2
            if direction[y][x] == 1:
                if y-1 < 0: break
                else: next_x = x; next_y = y-1
            elif direction[y][x] == 2:
                if x-1 < 0: break
                else: next_x = x-1; next_y = y
            elif direction[y][x] == 3:
                if x+1 > M-1: break
                else: next_x = x+1; next_y = y
            else:
                if y+1 > N-1: break
                else: next_x = x; next_y = y+1

            dq.append([next_y, next_x])
            count += 1
        elif visited[y][x] == 2:
            break

    if count != 0:
        print(count)
    else:
        print(-1)

if __name__=="__main__":
    main()

'''
1 상, 2 좌, 3 우, 4 하
'''