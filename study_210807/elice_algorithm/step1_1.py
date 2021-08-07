'''
청팀백팀
'''
team1 = map(int, input().split())
team2 = map(int, input().split())

sum1 = sum(team1)
sum2 = sum(team2)

print(max(sum1, sum2))
