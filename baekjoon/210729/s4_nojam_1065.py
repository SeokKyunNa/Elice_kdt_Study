'''
한수
'''
n = int(input())

# 100보다 작으면 모든 수가 한수
if n < 100:
    print(n)
    exit()

# 조건이 1000까지인데 1000은 한수가 아님
if n == 1000:
    n = 999

count = 99
x = 100

while x <= n:
    # 각 자리의 차를 계산
    if (x//100 - (x//10)%10) == ((x//10)%10 - x%10):
        count += 1
        x += 1
    else:
        x += 1
        pass
    
print(count)