'''
[수학] 바쁘다 바빠
'''
totalSec = 0
for _ in range(4):
    totalSec += int(input())

min = 0
sec = 0
min = totalSec // 60
sec = totalSec % 60

print(min)
print(sec)