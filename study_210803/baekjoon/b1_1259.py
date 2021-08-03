'''
팰린드롬수
'''
import sys

input = sys.stdin.readline
switch = 1

while 1:
    switch = 1
    num = int(input())
    if num == 0:
        break

    s_num = str(num)
    for i in range(len(s_num)//2):
        if s_num[i] == s_num[-1-i]:
            pass
        else:
            switch = 0
            break
    
    if switch == 0:
        print('no')
    else:
        print('yes')
