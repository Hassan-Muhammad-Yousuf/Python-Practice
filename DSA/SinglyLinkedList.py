class MyLinkedList:

  def __init__(self, value):
    self.head = {'value': value, 'next': None}
    self.tail = self.head
    self.length = 1
    # print(self.head)
    # print('==========================')

  def append(self, value):
    newNode = {'value': value, 'next': None}
    self.tail['next'] = newNode
    self.tail = newNode
    self.length += 1
    # print(newNode)
    # print('==========================')
    return self.length

  def prepend(self, value):
    newNode = {'value': value, 'next': None}
    newNode['next'] = self.head
    self.head = newNode
    self.length += 1
    return self.length

  def insert(self, index, value):
    if index >= self.length:
      return self.append(value)
    newNode = {'value': value, 'next': None}
    leader = self.traverseToIndex(index - 1)
    holdingPointer = leader['next']
    leader['next'] = newNode
    newNode['next'] = holdingPointer
    self.length += 1
    return self.length

  def traverseToIndex(self, index):
    currentNode = self.head
    counter = 0
    while counter != index:
      currentNode = currentNode['next']
      counter += 1
      #print(currentNode)
    return currentNode

  def remove(self, index):
    leader = self.traverseToIndex(index - 1)
    unwantedNode = leader['next']
    leader['next'] = unwantedNode['next']
    self.length -= 1
    return self.length

  def printList(self):
    array = []
    currentNode = self.head
    while currentNode != None:
      array.append(currentNode['value'])
      currentNode = currentNode['next']
    return print(array)


call = MyLinkedList(10)
call.append(5)
call.prepend(16)
call.append(6)
call.prepend(9)
call.insert(2, 99)
call.insert(10, 100)
call.remove(2)
print(call.printList())