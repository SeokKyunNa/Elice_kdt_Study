'''
수리공 항승
물이 세는 곳의 개수 N, 테이프의 길이 L
N과 L은 1,000보다 작거나 같고, 물이 새는 위치는 1,000보다 작거나 같은 자연수
'''
N, L = map(int, input().split())
cracks = list(map(int, input().split()))
cracks.sort()

result = 0
start = 0
end = 0

for i in range(N):
    if start < cracks[i] and cracks[i] < end:
        continue
    else:
        start = cracks[i] - 0.5
        end = cracks[i] + L - 0.5
        result += 1

print(result)
















# N, L = map(int, input().split())
# _list = list(map(int, input().split()))
# _list.sort()

# answer = 1
# start = _list[0]
# end = _list[0] + L

# for i in range(N):
#     if start <= _list[i] < end:
#         continue
#     else:
#         start = _list[i]
#         end = _list[i] + L
#         answer += 1

# print(answer)