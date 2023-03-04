n = int(input())
n_list = list(map(int, input().split(' ')))

numList = set(list(range(3, 1001, 2)))

output = {2}
procedure = 3

while procedure ** 2 < 1001 and len(numList) > 1:
    forDel = set(map(lambda x: x*procedure, range(1, int(1000/procedure)+1)))
    numList -= forDel
    output.add(procedure)
    procedure = min(list(numList))

output |= numList

output = sorted(list(output))

result = 0

for i in n_list:
    if i in output:
        result += 1

print(result)