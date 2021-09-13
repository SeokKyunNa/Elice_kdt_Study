'''
AC
'''
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())    # 입력 받을 케이스 수

for _ in range(T):
    backwards = True   # R(거꾸로) 체크할 boolean 변수
    result = '' # 출력용 변수
    p = input().rstrip()    # 명령어 입력
    N = int(input())    # 데이터 개수 입력
    dq = deque(input().rstrip().strip('[]').split(',')) # 데이터를 입력 받아서 덱 형태로 저장

    # 명령어 돌면서 연산
    for order in p:
        # R 명령이면 backwards 값을 뒤집어줌 (True or False)
        if order == 'R':
            backwards = not backwards
        # D 명령어
        else:
            # dq에 값이 없는데 pop해야한다면 result를 error로 찍어줌
            if len(dq) == 0 or (len(dq) == 1 and dq[0] == ''):
                result = 'error'
                break

            # backwards 값에 따라서 왼쪽 or 오른쪽 pop
            if backwards:
                dq.popleft()
            else:
                dq.pop()
    # 위에서 받은 결과값이 error가 아니라면 
    # backwards 값에 따라서 그대로 or 뒤집어서 결과값을 만들어줌
    if result != 'error':
        if backwards:
            result = '['+ ','.join(dq) +']'
        else:
            dq.reverse()
            result = '['+ ','.join(dq) +']'

    print(result)

