'''
주방장 도도새
'''
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
order = list(map(int, input().split()))
sumT = 0
orderNum = 0

for i in range(0, N):
    sumT += order[i]
    if sumT > T:
        orderNum = i
        break
    elif sumT == T:
        orderNum = i+1
        break

if sumT < T:
    orderNum = N

print(orderNum)


'''
(1≤N≤50, 1≤T≤500)
1 1
1
return 1

1 1 
2
return 0

'''