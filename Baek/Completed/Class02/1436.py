n = int(input())

class naming:
    def __init__(self):
        self.digit = 3
        self.location = 0
        self.result = 666
        self.first = 0
        self.last = 0
    
    def nextLv(self):
        if self.judgeDigit():
            self.digit += 1
            self.location += 1
            self.first = int('1' + ('0' * (self.digit - 4)))
            #print(f'in nextLv first: {self.first}, result: {self.result}, last: {self.last}')
            self.getResult()
        else:
            if self.digit - 3 != self.location: # last가 남아 있을 때
                if len(str(self.last + 1)) <= self.digit - 3 - self.location:
                    self.last += 1
                    self.getResult()
                else:
                    self.first = int(str(self.first) + ((self.digit - 3 - self.location) * '6')) + 1
                    self.location = self.digit - 3
                    self.last = 0
                    self.getResult()
            else: # last가 없을 때
                self.first += 1
                if str(self.first)[-1] == '6':
                    while str(self.first)[-1] == '6':
                        self.first = str(self.first)[:-1]
                        self.location -= 1
                        if self.first == '':
                            self.first = 0
                        else:
                            self.first = int(self.first)
                self.last = 0
                self.getResult()

    def judgeDigit(self):
        strResult = str(self.result)
        if self.digit - 3 == self.location:
            for c in strResult[:self.location]:
                if c != '9':
                    return False
            #print('Digit actived')
            return True
        return False

        

    def getResult(self):
        result = ''

        if self.first != 0:
            result += str(self.first)
        result += '666'
        if self.digit - 3 != self.location:
            result += str(self.last).zfill(self.digit - 3 - self.location)
        
        self.result = int(result)
        #print(f'first: {self.first}, result: {self.result}, last: {self.last}, location: {self.location}')

findResult = naming()

for i in range(n-1):
    findResult.nextLv()

print(findResult.result)