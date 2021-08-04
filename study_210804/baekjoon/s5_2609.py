'''
최대공약수와 최소공배수
'''
import sys

input = sys.stdin.readline

n1, n2 = map(int, input().split())
n1_original = n1
n2_original = n2
gcf = 0
lcm = 0

if n2 > n1:
    n1, n2 = n2, n1

while 1:
    if n1 % n2 != 0:
        n1, n2 = n2, (n1 % n2)
    else:
        gcf = n2
        break

print(gcf)

lcm = int((n1_original * n2_original) / gcf)
print(lcm)

