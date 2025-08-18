class DoublyLinkedList:

  def __init__(self, value):
    self.head = {'value': value, 'next': None, 'prev': None}
    self.tail = self.head
    self.length = 1
    # print(self.head)
    # print('==========================')

  def append(self, value):
    newNode = {'value': value, 'next': None, 'prev': None}
    newNode['prev'] = self.tail
    self.tail['next'] = newNode
    self.tail = newNode
    self.length += 1
    # print(newNode)
    # print('==========================')
    return self.length

  def prepend(self, value):
    newNode = {'value': value, 'next': None, 'prev': None}
    newNode['next'] = self.head
    self.head['prev'] = newNode
    self.head = newNode
    self.length += 1
    return self.length

  def insert(self, index, value):
    if index >= self.length:
      return self.append(value)
    newNode = {'value': value, 'next': None, 'prev': None}
    leader = self.traverseToIndex(index - 1)
    follower = leader['next']
    leader['next'] = newNode
    newNode['prev'] = leader
    newNode['next'] = follower
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
    follower = unwantedNode['next']
    leader['next'] = follower
    follower['prev'] = leader
    self.length -= 1

  def printList(self):
    array = []
    currentNode = self.head
    while currentNode != None:
      array.append(currentNode['value'])
      currentNode = currentNode['next']
    return print(array)


call = DoublyLinkedList(10)
call.append(5)
call.prepend(16)
# call.append(6)
# call.prepend(9)
# call.insert(2, 99)
call.insert(10, 100)
call.remove(2)
print(call.printList())