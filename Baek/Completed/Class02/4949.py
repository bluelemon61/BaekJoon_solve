open_bracket = ['(', '[']
close_bracket = [')', ']']

str_long = ''
while True:
  str_short = input()
  if str_short == '.':
    break
  str_long += str_short

str_list = list(str_long[:-1].split('.'))

#print(str_list)

for input_str in str_list:
    stack = []
    result = 'yes'
    for t in input_str:
        if t in open_bracket:
            stack.append(t)
            #print(stack)
        if t in close_bracket:
            if len(stack) < 1:
                result = 'no'
                break
            #print(ord(t), ord(stack[-1]))
            if t == ')':
                if ord(t) - ord(stack[-1]) == 1:
                    p = stack.pop()
                    #print(p)
                else:
                    result = 'no'
                    break
            if t == ']':
                if ord(t) - ord(stack[-1]) == 2:
                    p = stack.pop()
                    #print(p)
                else:
                    result = 'no'
                    break
    if len(stack) > 0:
        result = 'no'
    print(result)