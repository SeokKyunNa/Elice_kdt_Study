'''
스택 수열
'''
# 머리가 돌아갈 때 다시 풀기..
# 문제는 이해했는데 코드로 만들어내지를 못하는중
[4, 3, 6, 8, 7, 5, 2, 1]
import sys
from collections import deque
input = sys.stdin.readline

# N개 입력
N = int(input())
# 1 ~ N까지
dq = deque([n for n in range(1, N+1)])
# 입력 받을 수열 
progression = []
for _ in range(N):
    progression.append(int(input()))

result = []
while dq:
    index = 0
    if progression[index] == dq[len(dq)-1]:
        dq.pop()
        print('+')
    else:
        dq.append(dq.popleft())



'''
4 3 6 8 7 5 2 1

1 2 3 4 5 6 7 8
2 3 4 5 6 7 8 1
3 4 5 6 7 8 1 2
4 5 6 7 8 1 2 3
5 6 7 8 1 2 3 4
5 6 7 8 1 2 3 - 4
5 6 7 8 1 2 - 4 3
6 7 8 1 2 5
7 8 1 2 5 6
7 8 1 2 5 - 4 3 6
8 1 2 5 7
1 2 5 7 - 4 3 6 8
1 2 5 - 4 3 6 8 7
1 2 - 4 3 6 8 7 5
1 - 4 3 6 8 7 5 2
- 4 3 6 8 7 5 2 1
'''
