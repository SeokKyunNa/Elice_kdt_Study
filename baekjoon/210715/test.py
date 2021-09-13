# first 입력받은 정수
first = int(input())
second = 0

count = 0

if not (0 <= first <= 99):
    exit()

result = first

while True:
    if result < 10:
        result = str(first)[0] + str(first)[1]
    else:
        second = result % 10
        result = int(result/10)
        result = str(first)[-1] + str(second)[-1]
        
    result = int(result)
    count += 1

    if result == first :
        break
        

print(count)