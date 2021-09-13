'''
검증수
'''
_list = list(map(int, input().split()))
_listSquare = [n**2 for n in _list]

print(sum(_listSquare)%10)