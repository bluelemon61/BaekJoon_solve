A = int(input())
B = int(input())
C = int(input())

result = [0,0,0,0,0,0,0,0,0,0]
for n in str(A*B*C):
    result[int(n)] += 1

for i in result:
    print(i)