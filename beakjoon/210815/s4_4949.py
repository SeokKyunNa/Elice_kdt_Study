'''
균형잡힌 세상
'''
import sys
input = sys.stdin.readline

sentence = ''

while 1:
    sentence = input().rstrip()
    if sentence == '.':
        break
    result = 'yes'
    bracket = []

    for c in sentence:
        if c not in ['(', ')', '[', ']']:
            continue
        if c == '(' or c == '[':
            bracket.append(c)
        elif c == ')':
            if len(bracket) > 0 and bracket.pop() == '(':
                continue
            else:
                result = 'no'
                break
        elif c == ']':
            if len(bracket) > 0 and bracket.pop() == '[':
                continue
            else:
                result = 'no'
                break
            
    if len(bracket) > 0:
        result = 'no'

    print(result)
