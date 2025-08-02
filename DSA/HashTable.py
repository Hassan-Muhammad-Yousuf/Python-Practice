class HashTable:

    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        #print(hash)
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        #print(self.data)
        return self.data

    def get(self, key):
        address = self._hash(key)
        cB = self.data[address]
        if cB:
            for i in range(len(cB)):
                if cB[i][0] == key:
                    return cB[i][1]

    def keys(self):
        keyArr = []
        for i in range(len(self.data)):
            if self.data[i]:
                for j in self.data[i]:
                    #print(j[0])
                    keyArr.append(j[0])
        return keyArr


call = HashTable(50)
call.set('grapes', 10000)
call.set('apples', 24)
call.set('oranges', 12)
call.set('Bananas', 76)

print(call.get('grapes'))
print(call.get('apples'))
print(call.get('oranges'))
print(call.get('Bananas'))

print(call.keys())