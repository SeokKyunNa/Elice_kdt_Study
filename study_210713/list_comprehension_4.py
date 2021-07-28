# 값이 두개 들어있는 튜플을 담은 리스트를 받아 리스트를 생성하되,
# 튜플 내부의 값을 뒤집어서 저장하세요.
ref = [(2, 3), (1, 4), (5, 6), (6, 1), (2, 7)]

_list = []
for num in ref:
    _list.append((b, a))

print(_list)

# list comprehenstion
# expression for component in input_sequence <if statement>]
_list = [(b, a) for a, b in ref]

print(_list)