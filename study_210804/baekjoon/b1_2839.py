'''
설탕배달
'''
# 입력
kg = int(input())

# 초기값
num5 = kg // 5
remain = kg % 5

if remain == 1:
    num5 -= 1
    num3 = 2
elif remain == 2:
    if num5 == 1:   # 한 자리 숫자 7일때는 나올수 있는 조합이 없음
        num3 = -2
    else:
        num5 -= 2
        num3 = 4
elif remain == 4:
    if num5 == 0:   # 한 자리 숫자 4일때는 나올 수 있는 조합이 없음
        num3 = -1
    else:
        num5 -= 1
        num3 = 3
else:
    num3 = remain//3

print(num5+num3)

