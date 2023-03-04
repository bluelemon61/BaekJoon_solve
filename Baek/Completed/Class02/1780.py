import sys
n = int(sys.stdin.readline())
matrix = [0]*n
for i in range(n):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

result = [0, 0, 0]

def paper(matrix, step):
    combine = set()
    for i in range(step):
        combine |= set(matrix[i])
    
    if len(combine) == 1:
        for i in combine:
            result[i+1] += 1
    else:
        next_step = int(step/3)
        for i in range(0, step, next_step):
            for j in range(0, step, next_step):
                new_matrix = [0]*next_step
                for k in range(next_step):
                    new_matrix[k] = matrix[i+k][j:j+next_step]
                paper(new_matrix, next_step)

paper(matrix, n)
for i in result:
    print(i)