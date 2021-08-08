'''
K번 곱하기
'''
MUL = 1_000_000_009

N, K = map(int, input().split())
result = 0
for num in range(1, N+1):
    result += num**K % MUL


print(result)
