'''
부녀회장이 될테야
'''
'''
 103호 = 6명
 203호 = 10명
 1 2 3  4  5  6  7  8  9 ... 1, 1, 1, 1, ...
 1 3 6  10 15 21 28 36 45... 2, 3, 4, 5, 6, ...
 1 4 10 20 35 56 88 ........ 3, 6, 10, 15, 21, ...
 1 5 15 35 70 .............. 4, 10, 20, 35, ...
 1 6 21 56 126.............. 5, 15, 35, 70
'''
import sys
input = sys.stdin.readline

# 14층 14호가 마지막이기 때문에 전체 배열을 만들어둠
_list = [[n for n in range(0, 15)] for k in range(0, 15)]
for i in range(1, 15): # 층
    for j in range(1, 15): # 호
        _list[i][j] = _list[i][j-1] + _list[i-1][j]

# 층, 호수 입력 받아서 index로 출력
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(_list[k][n])
