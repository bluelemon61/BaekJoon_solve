expression = input()

expr = []
temp = ''
pm = {'+', '-'}
for t in expression:
    if t in pm:
        expr.append(int(temp))
        expr.append(t)
        temp = ''
    else:
        temp += t
expr.append(int(temp))

#print(expr)

result = expr[0]
expr.pop(0)
minus_flag = False
for i in expr:
    if i == '-':
        minus_flag = True
    else:
        if i != '+':
            if minus_flag:
                result -= i
            else:
                result += i

print(result)