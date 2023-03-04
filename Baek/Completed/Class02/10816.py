n = int(input())
n_list = list(map(int, input().split(' ')))

m = int(input())
m_list = list(map(int, input().split(' ')))

n_dic = {}
for i in n_list:
    if i in n_dic:
        n_dic[i] += 1
    else:
        n_dic[i] = 1

result = ''
for i in m_list:
    if i in n_dic:
        result += str(n_dic[i]) + ' '
    else:
        result += str(0) + ' '

print(result[:-1])