'''
영화감독 숌
'''
N = int(input())

for i in range(666, int(10_000_000)):
    if '666' in str(i):
        N -= 1

        if N == 0:
            print(i)
            break