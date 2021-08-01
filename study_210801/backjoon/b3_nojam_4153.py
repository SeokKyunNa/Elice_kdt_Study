'''
직각삼각형
'''
import sys

input = sys.stdin.readline

while 1:
    # 리스트 초기화
    num = [-1] * 3
    # 값 입력
    num[0], num[1], num[2] = map(int, input().split())
    # 1이상의 값만 입력되므로 세 수의 합이 0이면 break
    if sum(num) == 0:
        break

    # 세 숫자 중 제일 큰 값(빗변)
    c = max(num)
    num.remove(c)


    # 피타고라스의 정리 적용
    if num[0]**2 + num[1]**2 == c**2:
        print("right")
    else:
        print("wrong")

