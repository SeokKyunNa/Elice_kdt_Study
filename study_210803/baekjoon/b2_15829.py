'''
Hashing
'''
import sys

input = sys.stdin.readline
R = 31
M = 1_234_567_891

# 문자열의 길이 L
L = int(input())
# 입력 받은 문자열
word = input().rstrip()
# 해시값
hash_num = 0
index = 0

# ASCII 코드
# ord('a') = 97, ord('z') = 122
for c in word:
    hash_num += ((ord(c) - 96) * (R ** index))
    index += 1

print(hash_num%M)
