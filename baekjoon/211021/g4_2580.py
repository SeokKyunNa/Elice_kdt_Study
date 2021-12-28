'''
스도쿠
입력 : 9 x 9 형식의 숫자로 이루어진 문자열
'''
sudoku = [list(map(int, input().split())) for i in range(9)]
zeros = [(x, y) for x in range(9) for y in range(9) if sudoku[x][y]==0]

# print(zeros)

cnt = 0
currnt = 0

while True:
    if cnt==len(zeros):
        break
    
    x, y = zeros[cnt]
    for num in range(1, 10):

        # 가로 체크
        if num in sudoku[x]:
            continue

        # 세로 체크
        isBreak = False
        for i in range(9):
            # print(sudoku[i][y])
            if num == sudoku[i][y]:
                isBreak = True
                break
        if isBreak:
            continue

        # 3*3 체크
        X = x // 3
        Y = y // 3
        isBreak = False
        for i in range(X*3, X*3+3):
            for j in range(Y*3, Y*3+3):
                if num == sudoku[i][j]:
                    isBreak = True
                    break
            if isBreak:
                break
        if isBreak:
            continue
        
        current = num
        
    sudoku[x][y] = current
    cnt += 1

print()
for i in range(9):
    string_ints = [str(x) for x in sudoku[i]]
    print(' '.join(string_ints))
