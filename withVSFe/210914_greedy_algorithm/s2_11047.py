'''
동전 0
동전 N종류, K원 만들기
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
worth = []
for _ in range(N):
    worth.append(int(input().rstrip()))

count = 0
while K > 0:
    curr = worth.pop()
    if curr > K:
        continue
    count += K // curr
    K = K % curr

print(count)