'''
통계학
'''
# 답은 나오지만, 시간 초과 뜨는 함수
# Counter 사용하지 않고 작성
import sys
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

dict_count = {}
count = 0
new_list = list(set(list_num))
for n in new_list:
    count = list_num.count(n)
    if count == 0: continue
    if count in dict_count:
        dict_count[count].append(n)
    else:
        dict_count[count] = [n]

max_count = max(dict_count)
if len(dict_count[max_count]) == 1:
    print(dict_count[max_count][0])
else:
    dict_count[max_count].sort()
    print(dict_count[max_count][1])

# 범위
print(abs(max_num - min_num))