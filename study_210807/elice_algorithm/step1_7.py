'''
김 박사의 비밀 데이터
'''
import sys
input = sys.stdin.readline

N = int(input())
password = []
for _ in range(N):
    password.append(int(input()))

check_password = 0
for i in range(N):
    check_password += password[i]

print(str(check_password)[0:10])
