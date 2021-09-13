'''
깊은 산 속 옹달샘
'''
def main():
    N, M = map(int, input().split())
    forest = []
    visited = [[0 for n in range(M)] for n in range(N)]
    result = {}

    for i in range(N):
        forest.append(input())
    
    for i in range(N):
        for j in range(M):
            if forest[i][j] == 'S':
                S = [i, j]
            elif forest[i][j] == 'F':
                F = [i, j]

    print(forest)
    print(S, F)

if __name__=="__main__":
    main()