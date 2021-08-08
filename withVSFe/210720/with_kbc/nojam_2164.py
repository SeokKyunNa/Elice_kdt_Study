from collections import deque

# [1, 2, 3, 4, 5, ....., N]
# deque -> iterable한 데이터를 받을 수 있다.
# iterable : for문을 사용할 수 있다.

dq = deque(range(1, int(input()) + 1))

while len(dq) != 1:
    dq.popleft()    # 윗쪽에 있는 카드 삭제
    dq.append(dq.popleft())    # 윗쪽에 있는 카드를 삭제해서 아래로 보낸다.

print(dq[0])