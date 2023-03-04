import sys
n = int(sys.stdin.readline())

def push(queue, command):
    queue.append(int(command[1]))

def pop(queue, command):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop(0))

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
    'push': push,
    'pop': pop,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back,
}

queue = []

for i in range(n):
    command = sys.stdin.readline().split()
    command_list[command[0]](queue, command)