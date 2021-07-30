'''
소수찾기
'''
import sys
input = sys.stdin.readline

N = int(input())
_list = list(map(int, input().split()))

cnt = 0
for num in _list:
    # 1은 소수가 아니므로 넘어감
    if num == 1:
        continue

    # 1과 자신 외에 나눠지는 값을 체크하는 변수
    # 1로 바뀐다면 나눠지는 값이 있다는 의미
    tmp = 0
    # 2부터 num-1까지 나눠지는 값이 있는지 확인
    for d in range(2, num):
        # 나눠지는 값이 있다면 tmp를 1로 바꾸고 break
        if num % d == 0:
            tmp = 1
            break

    if tmp == 1:
        continue

    cnt += 1

print(cnt)
