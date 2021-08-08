h, m = map(int, input().split())

if m < 45:
    if h == 0:
        h = 24
    print(h-1, 60+m-45)
else:
    print(h, m-45)