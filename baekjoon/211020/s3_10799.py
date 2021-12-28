'''
쇠막대기
'''
# 필요한 변수: 총합, 현재 쇠막대기 수

import sys
input = sys.stdin.readline

def ironStick(value):
    current = 0
    total = 0
    for i in range(len(value)):
        if value[i] == '(':
            if value[i+1] == '(':
                current += 1
                total += 1
            else:
                total += current
                i += 1
        else:
            if value[i-1] == ')':
                current -= 1

    return total


value = input().rstrip()

print(ironStick(value))
