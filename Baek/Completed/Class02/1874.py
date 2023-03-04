n = int(input())
sequence = []
for i in range(n):
    sequence.append(int(input()))

def posibility(sequence):
    high = 0
    compare = 0
    for i in sequence:
        if i > high:
            high = i
        elif i > compare:
            return False
        compare = i
    return True

def stackOutput(sequence):
    stack = sorted(sequence)
    stack.insert(0, 0)
    index = 0
    result = ''
    for i in sequence:
        if stack[index] != i:
            if stack[index] > i:
                return ['NO']
            while stack[index] != i:
                index += 1
                result += '+'
            stack.pop(index)
            result += '-'
            index -= 1
        else:
            stack.pop(index)
            result += '-'
            index -= 1
    return result

if posibility(sequence):
    for i in stackOutput(sequence):
        print(i)
else:
    print('NO')