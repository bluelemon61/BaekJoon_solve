n = int(input())

wordList = {}
for i in range(n):
    word = input()
    wordList[word] = len(word)

lenList = []
for val in wordList.values():
    if val not in lenList:
        lenList.append(val)
lenList.sort()

result = []
for num in lenList:
    listInNum = []
    for word in wordList:
        if num == wordList[word]:
            listInNum.append(word)
    listInNum.sort()
    result.extend(listInNum)

for word in result:
    print(word)