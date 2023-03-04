channel = input()
n = int(input())
if n == 0:
    print(min(abs(int(channel)-100), len(channel)))
else:
    xbutton = sorted(list(map(int, input().split())))

    button = []
    for i in range(10):
        if i not in xbutton:
            button.append(i)
    routeOne = abs(int(channel) - 100)

    key_index = -1
    for i in range(len(channel)):
        if int(channel[i]) in xbutton:
            key_index = i
            break

    #print(button, xbutton, key_index)

    routeTwo = 0
    if key_index == -1:
        routeTwo = len(channel)
    elif len(button) == 1 and button[0] == 0:
        routeTwo = int(channel) + 1
    elif n == 10:
        routeTwo = routeOne
    else:
        digit = len(channel) - key_index

        highChannel = list(map(int, channel))
        for i in range(key_index+1, len(highChannel)):
            highChannel[i] = button[0]
        flag = False
        for i in reversed(range(key_index + 1)):
            if flag:
                highChannel[i] += 1
            flag = False
            while True:
                if highChannel[i] not in xbutton:
                    break
                highChannel[i] += 1
            if highChannel[i] > button[-1]:
                highChannel[i] = button[0]
                if i == 0:
                    if button[0] == 0:
                        highChannel = [button[1]] + highChannel
                    else:
                        highChannel = [button[0]] + highChannel
                flag = True

        lowChannel = list(map(int, channel))
        for i in range(key_index+1, len(lowChannel)):
            lowChannel[i] = button[-1]
        flag = False
        for i in reversed(range(key_index + 1)):
            if flag:
                lowChannel[i] -= 1
            flag = False
            while True:
                if lowChannel[i] not in xbutton:
                    break
                lowChannel[i] -= 1
            if lowChannel[i] < button[0]:
                lowChannel[i] = button[-1]
                if i == 0:
                    if len(lowChannel) == 1:
                        lowChannel = highChannel
                    else:
                        lowChannel = lowChannel[i+1:]
                flag = True
        
        #print(highChannel, lowChannel)

        highValue = int(''.join(map(str, highChannel)))
        lowValue = int(''.join(map(str, lowChannel)))

        highRoute = len(str(highValue)) + int(highValue)-int(channel)
        lowRoute = len(str(lowValue)) + abs(int(channel)-lowValue)
        #print(highRoute, lowRoute)
        routeTwo = (min(highRoute, lowRoute))
    
    #print(routeOne, routeTwo)
    print(min(routeOne, routeTwo))