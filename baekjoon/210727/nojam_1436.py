# silver 5 - 영화감독 숌
N = int(input())

for i in range(666, int(1e9)):
    if '666' in str(i):
        N -= 1
        if N == 0:
            print(i)
            exit()