T = int(input())

for _ in range(T):
    for i in range(3):
        _list = [[i, j, k] for i, j, k in input().split()]

print(_list)



'''
행 : i
열 : j
대각선 : i == j

1. i == 0에서 시작하고 모든 경우의 수 따지기
 
2. j == 0에서 시작하고 모든 경우의 수 따지기

3. i == j == 0에서 시작하고 모든 경우의 수 따지기

'''