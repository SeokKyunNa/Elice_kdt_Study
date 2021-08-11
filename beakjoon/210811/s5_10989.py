'''
수 정렬하기3
'''
import sys

N = int(sys.stdin.readline())
num_list = [0 for n in range(10001)]

for _ in range(N):
    num = int(sys.stdin.readline())
    num_list[num] += 1

for i in range(10001):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)

'''
딕셔너리로 풀어봤으나 시간초과 나옴
리스트 인덱스만 사용해야 하는 듯..
'''