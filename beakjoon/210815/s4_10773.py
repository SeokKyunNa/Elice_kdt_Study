'''
제로
'''
import sys
input = sys.stdin.readline

K = int(input())
balance = []

for _ in range(K):
    money = int(input())
    if len(balance) > 0 and money == 0:
        balance.pop()
    else:
        balance.append(money)

print(sum(balance))