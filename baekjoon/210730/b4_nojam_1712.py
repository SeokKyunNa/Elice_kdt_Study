'''
손익분기점
'''
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
    exit()

print(int(A / (C - B)) + 1)