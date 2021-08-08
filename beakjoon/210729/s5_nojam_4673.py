'''
셀프 넘버
'''
def d(n):
    return n+(n//10)+(n%10)

_set = (n for n in range(1, 10000))

n = 1
while d(n) <= 10000:
    for i in range(1, 10000):\
        if d(i) in range(1, ):
            print()
        else:
            pass

    n += 1