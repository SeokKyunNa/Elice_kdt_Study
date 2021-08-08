'''
단백질 바
'''
N = int(input())

if N%10 != 0:
    print(-1)
    exit()

nut = 0
chicken = 0
protein = 0

protein = N // 250
N = N % 250
chicken = N // 40
N = N % 40
nut = N // 10

print(nut, chicken, protein)