from collections import deque
import sys

def solution():
    func = sys.stdin.readline().rstrip()
    _ = sys.stdin.readline().rstrip()
    arr = deque(sys.stdin.readline().rstrip().strip('[]').split(','))

    flag = 0
    for c in func:
        if c == 'D':
            if not arr:
                print('error')
                return
            if flag == 0:
                arr.popleft()
            else:
                arr.pop()
        else:
            flag = 1 - flag

    if flag == 0:
        print('[' + ','.join(arr) + ']')
    else:
        print('[' + ','.join(arr[::-1]) + ']')

for i in range(int(input())):
    solution()
