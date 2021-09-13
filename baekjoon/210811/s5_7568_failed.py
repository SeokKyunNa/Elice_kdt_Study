'''
덩치
'''
import sys
input = sys.stdin.readline

N = int(input())
bulk = []

# 몇 번째 입력(i)인지와 키, 몸무게를 2차원 리스트에 입력 받음
for i in range(N):
    x, y = map(int, input().split())
    bulk.append([i, x, y])

# 몸무게 기준으로 정렬
def getKey(_list):
    return _list[1] # 몸무게
bulk.sort(key=getKey, reverse=True)

rank = 1
count = 1

# 몸무게 기준으로 정렬됐으므로
# 키만 비교해가면서 순위를 매김
for i in range(N):
    count += 1
    bulk[i].append(rank)
    # 마지막 인덱스는 더이상 비교할 대상이 없으므로 비교하지 않고 종료
    if i == N-1:
        continue
    if bulk[i][2] > bulk[i+1][2]:
        rank = count
            
# 입력했던 순서(위에서 입력한 0번째 값]대로 다시 정렬
bulk.sort()

# 리스트를 돌면서 등수만 뽑아서 리스트에 다시 담음
ranking = []
for i in range(N):
    ranking.append(str(bulk[i][3]))

# 등수 리스트를 string으로 출력
print(' '.join(ranking))

# 했으나 오답..
# 너무 복잡하게 생각했나보다..
# 풀이 방법은 등수를 구하는 것이 아니라
# 나보다 큰 사람이 몇명인가를 구하는 것이란다.