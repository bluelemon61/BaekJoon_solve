import sys
n = int(sys.stdin.readline())

def push(stack, command):
    stack.append(int(command[1]))

def pop(stack, command):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def size(stack, command):
    print(len(stack))

def empty(stack, command):
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top(stack, command):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
    
command_list = {
    'push': push,
    'pop': pop,
    'size': size,
    'empty': empty,
    'top': top,
}

stack = []

for i in range(n):
    command = sys.stdin.readline().split()
    command_list[command[0]](stack, command)