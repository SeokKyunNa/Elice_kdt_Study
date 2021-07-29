'''
더하기 사이클
'''
start = int(input())

tensDigit = start//10
unitDigit = start%10
count = 0
result = 0

while 1:
    result = tensDigit + unitDigit
    tensDigit = unitDigit
    unitDigit = result % 10
    count += 1
    if tensDigit*10 + unitDigit == start:
        break    

print(count)