'''
통계학
'''
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())

list_num = []
for _ in range(N):
    list_num.append(int(input()))

min_num = min(list_num)
max_num = max(list_num)
sum_num = sum(list_num)
len_num = len(list_num)

list_num.sort()
# 산숲평균
print(round(sum_num/len_num))

# 중앙값
print(list_num[len_num//2])

# 최빈값 (여러 개 있다면 최빈값 중 두 번째로 작은 값)
list_count = Counter(list_num).most_common()
if len(list_count)==1 or list_count[0][1] > list_count[1][1]:
    print(list_count[0][0])
else:
    print(list_count[1][0])

# 범위
print(abs(max_num - min_num))