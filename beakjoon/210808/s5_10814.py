'''
나이순 정렬
'''
import sys

input = sys.stdin.readline

N = int(input())
members = {}    # 입력 받을 딕셔너리

# members 딕셔너리의 key에 나이를 입력
# members 딕셔너리의 value에 이름을 list 형태로 입력(가입순으로 출력해야 함)
for i in range(N):
    age, name = input().split()
    age = int(age)
    if age not in members:
        members[age] = [name]
    else:
        members[age].append(name)

# 최대 200살까지 입력받을 수 있으므로 for문을 돌면서
# 나이에 해당하는 key가 있다면 차례대로(가입순) 출력
for age in range(201):
    if age in members:
        for name in members[age]:
            print(age, name)