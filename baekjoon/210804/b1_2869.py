'''
달팽이는 올라가고 싶다
'''
A, B, V = map(int, input().split())
day = 0
remain = V - A
day = remain//(A-B)

if remain%(A-B) == 0:
    day += 1
else:
    day += 2

print(day)