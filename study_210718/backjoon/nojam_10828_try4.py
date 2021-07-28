class Stack:
    def __init__(self, num):
        self.arr = []
        self.arr = [None] * num
        self.stacktop = -1

    def push(self, data):
        self.stacktop += 1
        self.arr[self.stacktop] = data
        return

    def pop(self):
        if self.empty():
            return -1

        data = self.arr[self.stacktop]
        self.stacktop -= 1

        return data

    def size(self):
        return self.stacktop + 1

    def empty(self):
        if self.stacktop == -1:
            return 1
        else:
            return 0
    
    def top(self):
        if self.empty():
            return -1
        
        return self.arr[self.stacktop]

num = int(input())
cnt = 1
myStack = Stack(num)

while cnt <= num:
    order = input().split()

    if order[0] == 'push':
        myStack.push(int(order[1]))
    elif order[0] == 'pop':
        print(myStack.pop())
    elif order[0] == 'size':
        print(myStack.size())
    elif order[0] == 'empty':
        print(myStack.empty())
    elif order[0] == 'top':
        print(myStack.top())

    cnt += 1