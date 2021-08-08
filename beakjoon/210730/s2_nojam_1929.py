'''
소수 구하기
'''
M, N = map(int, input().split())

# M부터 N까지 돌면서 소수인지 확인
for num in range(M, N+1):
    if num == 1:
        continue

    switch = 0
    for d in range(2, num):
        if num % d == 0:
            switch = 1
            break
    
    if switch == 1:
        continue

    print(num)