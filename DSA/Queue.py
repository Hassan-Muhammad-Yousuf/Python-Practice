class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def peek(self):
    return self.first.value if self.first else None

  def enqueue(self, value):
    newNode = Node(value)
    if self.length == 0:
      self.first = newNode
      self.last = newNode
    else:
      self.last.next = newNode
      self.last = newNode
    self.length += 1
    return self.length

  def dequeue(self):
    if self.length == 0:
      return None
    if self.first == self.last:
      self.last = None
    holdingPointer = self.first
    self.first = self.first.next
    self.length -= 1
    return holdingPointer.value
  
  def __str__(self):
    if self.length == 0:
      return "Queue is empty"
    values = []
    currentNode = self.first
    while currentNode:
      values.append(str(currentNode.value))
      currentNode = currentNode.next
    return " <- ".join(values)

q = Queue()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
q.enqueue(13)
print(q)
q.dequeue()
q.dequeue()
print(q)