'''
카드2
'''
from collections import deque

# 1 ~ N+1까지의 카드를 덱에 넣음
N = int(input())
card = deque([i for i in range(1, N+1)])

# 카드를 돌면서 제일 앞의 숫자는 빼고, 
# 그 다음 숫자는 꺼내서 맨뒤에 다시 넣는 것을 반복
# 1장만 남으면 멈춤
while len(card) > 1:
    card.popleft()
    if len(card) > 1:
        card.append(card.popleft())

print(*card)