'''
덱
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    order = list(map(str, input().split()))
    if len(order) > 1:
        order[1] = int(order[1])

    # push_back
    if order[0] == 'push_back':
        dq.append(order[1])

    # push_front
    if order[0] == 'push_front':
        dq.appendleft(order[1])

    # pop_front
    elif order[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    # pop_back
    elif order[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    # size
    elif order[0] == 'size':
        print(len(dq))

    # empty
    elif order[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    # front
    elif order[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    # back
    elif order[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq)-1])