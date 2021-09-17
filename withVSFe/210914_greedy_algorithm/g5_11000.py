'''
강의실 배정
'''
import heapq
import sys
input = sys.stdin.readline

N = int(input())
time = [tuple(map(int, input().split())) for _ in range(N)]

time.sort()

heap = []
heapq.heappush(heap, time[0][1])

for i in range(1, N):
    start, end = time[i]
    if heap[0] > start:
        heapq.heappush(heap, end)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, end)

print(len(heap))
# print(heap)