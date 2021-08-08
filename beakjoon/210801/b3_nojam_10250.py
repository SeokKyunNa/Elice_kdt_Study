'''
ACM 호텔
'''
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    #층
    if N % H == 0:
        YY = H
    else:
        YY = N % H

     # 호수
    if N % H == 0:
        XX = N // H
    else:
        XX = N // H + 1
    
    # 호수 YYXX
    print(YY*100 + XX)