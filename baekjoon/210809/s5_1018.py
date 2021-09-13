'''
체스판 다시 칠하기
'''
import sys
input = sys.stdin.readline

# N은 줄, M은 칸
N, M = map(int, input().split())
# 전체 체스판 입력
board = [input() for _ in range(N)]

# 좌표 x, y의 합(x+y)이 짝수일 때와 홀수일 때로 나눠서 연산
def check(graph):
    result1 = 0
    result2 = 0
    # 8x8 체스판을 읽음
    for i in range(8):
        for j in range(8):
            # 좌표의 합이 짝수이고
            if (i+j) % 2 == 0:
                # 해당 좌표의 값이 B(Black)라면
                if graph[i][j] == 'B':
                    # result1을 증가
                    result1 += 1
                # 해당 좌표의 값이 W(White)라면
                else:
                    # result2를 증가
                    result2 += 1
            # 좌표의 합이 홀수이고
            else:
                # 해당 좌표의 값이 B(Black)라면
                if graph[i][j] == 'B': 
                    # result2를 증가
                    result2 += 1
                # 해당 좌표의 값이 W(White)라면
                else:
                    # result1을 증가
                    result1 += 1

    # 둘 중 더 작은 값을 return
    return min(result1, result2)

answer = 100

# 입력 받은 전체 체스판에서 8x8을 만들 수 있는 동안 연산 수행
for i in range(N - 7):
    for j in range(M - 7):
        # 8x8 리스트를 graph에 담아서 check 함수에 인자로 넣어줌
        graph = [board[x][j: j + 8] for x in range(i, i + 8)]
        answer = min(answer, check(graph))

print(answer)
