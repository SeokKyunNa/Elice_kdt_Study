#N = 입력받은 정수(0-99)
N = input()

#cur = 새로운 수 
cur = int(N) if int(N) < 10 else int(N[0]) + int(N[1])
cur = N[-1] + str(cur)[-1]

#cnt = 사이클의 길이
cnt = 1

while int(cur) != int(N):
    past = cur
    cur = int(past) if int(past) < 10 else int(past[0]) + int(past[1])

    cur = past[-1] + str(cur)[-1]
    cnt += 1

print(cnt)