data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*data)

test_str = "Hello"
a, *rest, b = test_str
print(a, b)
print(rest)

test_str = "Hello"
print(test_str * 3)