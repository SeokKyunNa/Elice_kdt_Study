import sys

def checkParen(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 'NO'
            else:
                stack.pop(len(stack)-1)

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

input = sys.stdin.readline
N = int(input())

for _ in range(N):
    print(checkParen(input().rstrip()))

