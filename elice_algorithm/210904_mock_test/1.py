'''
시험
red : 1234512345
blue : 5432154321
yellow : 3333333333
N : 시험 문제 수
answer : 시험 문제 정답
'''

def main():
    # 입력
    N = int(input())
    answer = [int(n) for n in input()]

    # 각각의 답 생성
    answer_red = [5 if (n+1)%5==0 else (n+1)%5 for n in range(N)]
    temp = [5, 4, 3, 2, 1]
    if N >= 5:
        answer_blue = temp * (N//5) + temp[:N%5]
    else:
        answer_blue = temp[:N%5]
    answer_yellow = [3] * N

    # 각각의 개수 초기화
    counts = [0, 0, 0]

    for i in range(N):
        if answer_red[i] == answer[i]:
            counts[0] += 1
        if answer_blue[i] == answer[i]:
            counts[1] += 1
        if answer_yellow[i] == answer[i]:
            counts[2] += 1

    max_score = max(counts)
    print(max_score)

    players = ['red', 'blue', 'yellow']
    for i in range(3):
        if counts[i] == max_score:
            print(players[i])

if __name__=="__main__":
    main()
    