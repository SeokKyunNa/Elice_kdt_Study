'''
생수통
'''
import sys

input = sys.stdin.readline

body = []
head = []
for _ in range(3):
    body.append(int(input()))
for _ in range(2):
    head.append(int(input()))

min_body = min(body)
min_head = min(head)

print(min_body+min_head+10)