[m, n] = map(int, input().split(' '))

numList = set(list(range(3, n+1, 2)))

output = {2}
procedure = 3

while procedure ** 2 < n and len(numList) > 1:
    forDel = set(map(lambda x: x*procedure, range(1, int(n/procedure)+1)))
    numList -= forDel
    output.add(procedure)
    procedure = min(list(numList))

output |= numList

output = sorted(list(output))
if len(output) != 0:
    while output[0] < m:
        output.pop(0)

for i in output:
    print(i)