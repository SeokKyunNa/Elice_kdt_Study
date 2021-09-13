'''
프린터 큐
'''
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    dq = deque(map(int, input().split()))