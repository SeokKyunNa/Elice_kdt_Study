'''
벌집
'''
# 1, 7, 19, 37, 61, ...
# 6, 12, 18, 36, ...
# 첫째항이 6이고, 공차가 6인 등차수열
# max = n[i] + 6 * i 
# 0+1, 1+6, 7+12, ...
# index = N // 6
# if n & 6 != 0: index + 1

findN = int(input())
n = [1]

if findN == 1: print(1); exit()

for i in range(findN):
    if n[i] + (6*(i+1)) >= findN:
        print(i+2)
        exit()
    else:
        n.append(n[i] + (6*(i+1)))