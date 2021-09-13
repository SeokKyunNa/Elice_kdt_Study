'''
스택 수열
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
count = 0
stack = []
result = []
possible=True

for i in range(N):
    p = int(input())

    while count < p:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == p:
        stack.pop()
        result.append("-")
    else:
        possible = False
        continue

if possible == False:
    print("NO")
else:
    for o in result:
        print(o)



'''
4 3 6 8 7 5 2 1

1 2 3 4 5 6 7 8
2 3 4 5 6 7 8 | 1
3 4 5 6 7 8 | 1 2
4 5 6 7 8 | 1 2 3
5 6 7 8 | 1 2 3 4
5 6 7 8 | 1 2 3 - 4
5 6 7 8 | 1 2 - 4 3
6 7 8 | 1 2 5
7 8 | 1 2 5 6
7 8 | 1 2 5 - 4 3 6
8 | 1 2 5 7
| 1 2 5 7 - 4 3 6 8
| 1 2 5 - 4 3 6 8 7
| 1 2 - 4 3 6 8 7 5
| 1 - 4 3 6 8 7 5 2
- 4 3 6 8 7 5 2 1

1 2 5 3 4

1 2 3 4 5
2 3 4 5 | 1
2 3 4 5 - 1
3 4 5 | 2 - 1
3 4 5 - 1 2
4 5 | 3 - 1 2
5 | 3 4 - 1 2
| 3 4 5 - 1 2
| 3 4 - 1 2 5

'''

