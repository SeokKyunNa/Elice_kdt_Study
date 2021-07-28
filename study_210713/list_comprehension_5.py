# 주어진 리스트를 그대로 담되, 15가 넘어가는 값은 15로 저장하는 리스트를 만들어 봅시다.
ref = [2, 4, 16, 15, 13, 12, 11, 16, 14]

_list = []
for num in ref:
    if num > 15:
        _list.append(15)
    else:
        _list.append(num)

print(_list)

# list comprehenstion
# expression for component in input_sequence <if statement>]
_list = [num if num <= 15 else 15 for num in ref]

print(_list)