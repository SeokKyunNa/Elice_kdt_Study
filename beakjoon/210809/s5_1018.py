'''
체스판 다시 칠하기
'''
import sys
input = sys.stdin.readline

# N은 줄, M은 칸
N, M = map(int, input().split())
board = [input() for _ in range(N)]

def check(graph):
    result1 = 0
    result2 = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if graph[i][j] == 'B':
                    result1 += 1
                else:
                    result2 += 1
            else:
                if graph[i][j] == 'B': 
                    result2 += 1
                else:
                    result1 += 1
    return min(result1, result2)

answer = 100

for i in range(N - 7):
    for j in range(M - 7):
        graph = [board[x][j: j + 8] for x in range(i, i + 8)]
        answer = min(answer, check(graph))

print(answer)