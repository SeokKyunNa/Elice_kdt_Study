num = int(input())
n = num
cnt = 0
# 1의자리를 10의자리로
# 1의자리와 10의자리 더한수의 모드값을 1의자리로
while True:
    ten = n//10
    one = n % 10
    
    total = ten + one
    new_one = total % 10

    n = int(str(one) + str(new_one))

    cnt += 1
    if(num == n):
        break
print(cnt)