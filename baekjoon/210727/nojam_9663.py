

N = int(input())
answer = 0

def solution(data):
    global answer

    if len(data) == N:
        answer += 1
        return
    
    for i in range(1, N + 1):
        isOk = True
        # 대각선으로 만날때
        # if j - i == abs(data[i] - data[j])
        for j in range(len(data)):
            # 두 위치가 같으면 안 됨
            # 대각선으로 만나면
            # 길이는 항상 마지막 index보다 1 크다는 것을 사용한 꼼수
            if data[j] == i or len(data) - j == abs(i - data[j]):
                isOk = False
                break

        if isOk:
            data.append(i)
            solution(data)
            data.pop()

solution([])
print(answer)
