'''
배
'''
# 다음에 다시 풀어보기
import sys
from collections import deque
input = sys.stdin.readline

# 크레인 입력
N = int(input())
cranes = list(map(int, input().split()))

# 박스 입력
M = int(input())
boxes = list(map(int, input().split()))

# 불가능 출력
if max(boxes) > max(cranes):
    print(-1)

# 정렬
cranes.sort()
boxes.sort()
boxes = deque(boxes)

possible = {}
for crane in cranes:
    possible[crane] = []

i = 0
for crane in cranes:
    while boxes:
        box = boxes.popleft()
        if box < crane:
            possible[crane].append(box)
        else:
            break
    
print(possible)

