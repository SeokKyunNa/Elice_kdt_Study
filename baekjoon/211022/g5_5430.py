'''
AC
'''
from collections import deque
import sys
input = sys.stdin.readline

def ac():

    str_functions = input().rstrip()
    n = int(input())
    dq = deque(input().rstrip()[1:-1].split(','))
    switch=1

    for c in str_functions:
        if c=='R':
            switch *= -1
        else:
            if len(dq) <= 0 or dq[0]=='':
                return 'error'
            else:
                if switch > 0:
                    dq.popleft()
                else:
                    dq.pop()

    if switch < 0:
        dq.reverse()
    
    result = '['+','.join(list(dq))+']'
    return result

def main():
    T = int(input())
    for i in range(T):
        print(ac())

if __name__ == '__main__':
    main()

