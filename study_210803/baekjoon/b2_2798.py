'''
블랙잭
'''
import sys

input = sys.stdin.readline

# N은 주어질 카드의 개수
# M은 가장 가깝게 만들어야할 숫자
N, M = map(int, input().split())

_list = list(map(int, input().split()))
sum_list = [M]

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_list.append(_list[i] + _list[j] + _list [k])

sum_list.sort()
idx = sum_list.index(M)
if idx == len(sum_list)-1:
    print(sum_list[idx-1])
    exit()

if sum_list[idx+1] == M:
    print(M)
else:
    print(sum_list[idx-1])



