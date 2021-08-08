myStack = []
num = int(input())
cnt = 1

while cnt <= num:
    order = input().split()

    if order[0] == 'push':
        myStack.append(int(order[1]))
    elif order[0] == 'pop':
        if not myStack:
            print(-1)
        else:
            print(myStack.pop())
    elif order[0] == 'size':
        print(len(myStack))
    elif order[0] == 'empty':
        if not myStack:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if not myStack:
            print(-1)
        else:
            print(myStack[-1])

    cnt += 1
    
