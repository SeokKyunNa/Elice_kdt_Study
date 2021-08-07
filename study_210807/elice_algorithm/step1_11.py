'''
[수학] 도어락 비밀번호
'''
N1, N2 = map(str, input().split())

N1 = N1[::-1]
N2 = N2[::-1]

password = int(N1) + int(N2)

print(password)