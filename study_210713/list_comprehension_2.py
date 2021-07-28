# 2, 4, 6, 8, ... , 20을 담는 리스트를 만들어봅시다.
_list = []
for num in range(1, 11):
    _list.append(num*2)

print(_list)

# list comprehenstion
# expression for component in input_sequence <if statement>]
_list = [num * 2 for num in range(1, 11)]

print(_list)