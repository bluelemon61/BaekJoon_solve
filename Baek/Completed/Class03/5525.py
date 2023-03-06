n = int(input())
m = int(input())
s = input()

p_list = []
I = False
p_length = -1
for t in s:
    if t == 'I': # I
        if I: # if front t is I
            p_list.append(p_length)
            p_length = 0
        else:
            p_length += 1
        I = True
    else: # O
        if not I:
            p_list.append(p_length)
            p_length = -1
        I = False
p_list.append(p_length)

result = 0
for i in p_list:
    if i >= n:
        result += (i+1) - n

#print(p_list)
print(result)