'''
새로운 달력
'''
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

# 2차원 리스트에 달력을 직접 그리면서
# 마지막에 사용한 y값(1차원 인덱스 값)+1 을 출력함
# 알고리즘 분류가 수학, 정수론인거로 봐서는 식을 세워야 하는 듯..?
for case in range(T):
    month, md, wd = map(int, input().split())

    totalDay = deque([n for n in range(1,md+1)] * month)
    calendar = [[0 for _ in range(wd)] for _ in range(month*md)]

    x = -1
    y = -1
    while totalDay:
        day = totalDay.popleft()
        if day == 1:
            x = x+1
            if x >= wd:
                x = 0
            y = y+1
            calendar[y][x] = day
        else:
            x = x+1
            if x >= wd:
                x = 0
                y = y+1
            calendar[y][x] = day
        


    print('Case #' + str(case+1) + ': ' + str(y+1))
