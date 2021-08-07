'''
숫자 카드2
'''
import sys
input = sys.stdin.readline

# 들고있는 카드 입력
N = int(input())
n_list = list(map(int, input().split()))
# 딕셔너리에 넣어서 key=카드숫자, value=몇 장인지 입력
n_dict = {}
for card in n_list:
    if not card in n_dict:
        n_dict[card] = 1
    else:
        n_dict[card] += 1

# 확인할 숫자 입력
M = int(input())
m_list = list(map(int, input().split()))
# 숫자를 돌면서 위의 딕셔너리에서 value 값만 꺼내서 result에 넣음
# key:value 쌍이 없다면 0을 넣음
result = []
for num in m_list:
    if not num in n_dict:
        result.append(0)
    else:
        result.append(n_dict[num])

print(*result)