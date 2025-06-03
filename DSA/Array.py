class newArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem
    def get(self, index):
        return self.data[index]
    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        return item
    def shiftItems(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
    def __str__(self):
        return str(self.__dict__)
        #return str(self.data)
a = newArray()
a.push('hi')
a.push('you')
a.push('!')
a.delete(1)
print(a)
