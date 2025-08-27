class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    return self.top

  def push(self, value):
    newNode = Node(value)
    if self.length == 0:
      self.top = newNode
      self.bottom = newNode
    else:
      holdingPointer = self.top
      self.top = newNode
      self.top.next = holdingPointer
    self.length += 1
    return self.length

  def pop(self):
    if self.length == 0:
      return None
    if self.length == 1:
      self.bottom = None
      self.top = None
      self.length -= 1
      return self.length
    else:
      holdingPointer = self.top
      self.top = self.top.next
      self.length -= 1
      return holdingPointer.value

  def isEmpty(self):
    return self.length == 0  

  def __str__(self):
    values = []
    current = self.top
    while current:
      values.append(current.value)
      current = current.next
    return " -> ".join(map(str, values))



st = Stack()
print(st.push(10))   
print(st.push(20))   
print(st.push(30))   

print(st)            
print(st.peek().value) 
print(st.pop())      
print(st)            
print(st.isEmpty())  