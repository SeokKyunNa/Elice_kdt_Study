'''
단어 정렬
'''
import sys

input = sys.stdin.readline

N = int(input())
# 최대 50단어 이므로 51개([1][51])의 빈 리스트를 만듦
words = [[] for i in range(50+1)]   

# 각 인덱스와 단어길이를 매칭시켜서 단어를 append
for _ in range(N):
    word = input().rstrip()
    index = len(word)
    words[index].append(word)

# 각 인덱스(문자 길이)의 데이터를 꺼내서 중복을 제거하고 출력
for word in words:
    word = list(set(word))  # 중복 제거
    word.sort()
    for i in range(len(word)):
        print(word[i])