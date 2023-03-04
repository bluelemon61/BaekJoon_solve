while True:
    inNum = input()

    if inNum == '0':
        break

    result = 'yes'

    for i in range(len(inNum)):
        if i > len(inNum) - 1 - i:
            break
        if inNum[i] != inNum[-(1+i)]:
            result = 'no'
            break

    print(result)