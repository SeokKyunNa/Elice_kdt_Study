'''
좌표 정렬하기 2
'''
import sys
input = sys.stdin.readline

# N개 입력
N = int(input())

# y값을 key, x값을 value 로 갖도록 데이터 입력 및 저장
dict_num = {}
for _ in range(N):
    x, y = map(int, input().split())
    if y in dict_num:
        dict_num[y].append(x)
    else:
        dict_num[y] = [x]

# 전체를 돌 필요없으므로 최소값부터 최대값까지만 확인
min_dict = min(dict_num)
max_dict = max(dict_num)

# 딕셔너리의 최소값부터 최대값까지 돌면서
# 데이터가 있다면 해당 y좌표의 x 좌표를 정렬해서
# 작은 값부터 출력
for i in range(min_dict, max_dict+1):
    if i in dict_num:
        dict_num[i].sort()
        for j in range(len(dict_num[i])):
            print(dict_num[i][j], i)