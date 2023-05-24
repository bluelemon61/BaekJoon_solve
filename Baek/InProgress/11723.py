import sys
m = int(sys.stdin.readline())
s = set()


def add(x):
    s.add(x)
def remove(x):
    s.discard(x)
def check(x):
    # print(s)
    if x in s:
        print(1)
    else:
        print(0)
def toggle(x):
    if x in s:
        s.discard(x)
    else:
        s.add(x)
def all():
    s.clear()
    for i in range(1, 21):
        s.add(i)
    # print(s)
def empty():
    s.clear()

command = {
    'add': add,
    'remove': remove,
    'check': check,
    'toggle': toggle,
    'all': all,
    'empty': s.clear
}

for i in range(m):
    t = sys.stdin.readline().split()
    if len(t) == 2:
        command[t[0]](int(t[1]))
    else:
        command[t[0]]()