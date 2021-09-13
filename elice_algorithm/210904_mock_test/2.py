'''
해치웠나...
괄호 짝 맞추기
성공은 YES, 실패는 NO
'''
def main():
    bracket = input()
    stack = []
    result = ''
    for c in bracket:
        if c == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                result = 'NO'
                break
            
    if not stack and result != 'NO':
        result = 'YES'
    else:
        result = 'NO'

    print(result)


if __name__=="__main__":
    main()