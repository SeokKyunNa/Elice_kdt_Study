'''
음계
'''
scale = list(map(int, input().split()))

if scale[0] not in[1, 8]:
    print('mixed')
    exit()

result = ''

if scale[0] == 1:
    for i in range(0, 8):
        if scale[i] != i+1:
            result = 'mixed'
            break
        else:
            result = 'ascending'

else:
    for i in range(0, 8):
        if scale[i] != 8-i:
            result = 'mixed'
            break
        else:
            result = 'descending'

print(result)
