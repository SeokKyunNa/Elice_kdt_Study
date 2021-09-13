# 주어진 리스트를 받아 3의 배수인 값만 저장하는 리스트를 만들어봅시다.
ref = [23, 42, 15, 67, 83, 81]

_list = []
for num in ref:
    if num % 3 == 0:
        _list.append(num)

print(_list)

# list comprehenstion
# expression for component in input_sequence <if statement>]
ref = [23, 42, 15, 67, 83, 81]
_list = [num for num in ref if num%3 == 0]

print(_list)