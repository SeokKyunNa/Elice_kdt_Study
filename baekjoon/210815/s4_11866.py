'''
요세푸스 문제 0
'''
from collections import deque

N, K = map(int, input().split())

dq = deque([str(n) for n in range(1, N+1)])
result = []

while dq:
    for _ in range(K-1):
        dq.append(dq.popleft())
    result.append(dq.popleft())

str_result = ', '.join(result)
print('<' + str_result + '>')