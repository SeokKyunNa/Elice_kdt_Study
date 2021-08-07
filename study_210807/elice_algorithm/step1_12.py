'''
[수학] 덧셈을 모르는 체셔
'''

num = input()
result = 0

if len(num) == 4:
    result = 20
elif len(num) == 3:
    if num[0:2] == '10':
        result = int(num[:2]) + int(num[2])
    else:
        result = int(num[0]) + int(num[1:])
else:
    result = int(num[0]) + int(num[1])

print(result)