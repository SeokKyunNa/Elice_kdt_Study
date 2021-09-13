'''
1로 만들기
'''
N = int(input())
count = 0

while N != 1:
    if N >= 3:
        if N % 3 == 0:
            N = N / 3
            count += 1
            continue
        else:
            N = N -1
            count += 1
            continue
    elif N == 2:
        count += 1
        break

print(count)