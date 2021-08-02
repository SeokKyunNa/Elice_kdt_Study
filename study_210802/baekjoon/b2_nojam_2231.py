'''
분해합
'''
M = int(input())

for num in range(M):
    if M == num + sum([int(n) for n in str(num)]):
        print(num)
        exit()
    
print(0)
