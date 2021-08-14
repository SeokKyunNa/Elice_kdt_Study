'''
큐
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
    # push
    if order[0] == 'push':
        dq.append(order[1])

    # pop
    elif order[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

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