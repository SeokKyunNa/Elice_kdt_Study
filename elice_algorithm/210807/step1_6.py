'''
숫자 나라 특허 전쟁
'''
N = int(input())

sum = 0

for num in range(1, N):
    if num % 3 == 0 and num % 5 == 0:
        sum += num
    elif num % 3 == 0:
        sum += num
    elif num % 5 == 0:
        sum += num

print(sum)
