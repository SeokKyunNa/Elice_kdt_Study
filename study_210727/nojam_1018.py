## 실버 5 - 체스판 다시 칠하기 (1018)

N, M = map(int, input().split())

data = [input(0 for i in range(N))]

answer = int(1e9)

for i in range(N - 7):
    for j in range(M - 7):
        graph = [data[x][j: j+ 8] for x in range(i, i +8)]
        
        graph_alter = []
        for x in range(i, i + 8):
            graph_alter.append(data[x][j: j + 8])
        answer = min(answer, check(graph))





'''
graph라는 배열에 데이터를 8줄 넣을거다. 
'''