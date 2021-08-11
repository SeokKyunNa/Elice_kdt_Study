'''
덩치
'''
import sys
input = sys.stdin.readline

N = int(input())
bulk = []

# 입력
for i in range(N):
    x, y = map(int, input().split())
    bulk.append([x, y])

# 등수를 저장할 리스트
ranking = []

# 각각의 덩치를 전부와 비교
for i in range(N):
    rank = 1    # 등수는 1부터 시작
    for j in range(N):
        # 전체를 돌면서 나보다 큰 덩치가 있을때마다 등수를 1씩 증가시킴
        if bulk[i][0] < bulk[j][0] and bulk[i][1] < bulk[j][1]:
            rank += 1
    # 비교가 끝나면 등수를 ranking 리스트에 입력
    ranking.append(str(rank))

# ranking 리스트를 문자열로 치환하여 출력
print(*ranking)
# print(' '.join(ranking))


