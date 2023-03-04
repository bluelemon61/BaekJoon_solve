import sys
n = int(sys.stdin.readline())

def push_front(queue, command):
    queue.insert(0, int(command[1]))

def push_back(queue, command):
    queue.append(int(command[1]))

def pop_front(queue, command):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop(0))

def pop_back(queue, command):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop())

def size(queue, command):
    print(len(queue))

def empty(queue, command):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue, command):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back(queue, command):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])
    
command_list = {
    'push_front': push_front,
    'push_back': push_back,
    'pop_front': pop_front,
    'pop_back': pop_back,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back,
}

deque = []

for i in range(n):
    command = sys.stdin.readline().split()
    command_list[command[0]](deque, command)