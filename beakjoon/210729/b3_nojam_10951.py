'''
A+B -4
'''
import sys
input = sys.stdin.readline

while 1:
    n = input().rstrip()
    if n == '':
        exit()
    a, b = map(int, n.split())
    print(a+b)