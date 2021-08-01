'''
직사각형에서 탈출
'''
x, y, w, h = map(int, input().split())

# x 좌표에서 왼쪽과 오른쪽 중 더 가까운 값
w_min = min(x, w-x)
# y 좌표에서 아래와 위 중 더 가까운 값
h_min = min(y, h-y)

#가장 가까운 값
print(min(w_min, h_min))