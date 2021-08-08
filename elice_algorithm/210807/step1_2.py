'''
도도새의 업무일지
'''
N = int(input())
B = list(map(int, input().split()))
A = [B[0]]
sumA = 0

for i in range(1, N):
    sumA = sum(A)
    num = B[i] * (i+1) - sumA
    A.append(num)

print(*A)



'''
제작 1, 3, 2, 6, 8
평균 1, 2, 2, 3, 4


2 = 1+3/2
create1 / day1 = 1
create1 + create2 / day2 = 2
create1 + create2 + create3 / day3 = 3
...
'''