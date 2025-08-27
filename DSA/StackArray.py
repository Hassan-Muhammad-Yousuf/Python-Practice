class StackArr:
  def __init__(self):
    self.array = []

  def peek(self):
    return self.array[-1] if self.array else None

  def push(self, value):
    self.array.append(value)

  def pop(self):
    return self.array.pop() if self.array else None

  def isEmpty(self):
    return len(self.array) == 0  

  def __str__(self):
    return " -> ".join(map(str, reversed(self.array)))




st = StackArr()
st.push(10)
st.push(11)
st.push(12)
st.push(13)
print(st)
st.pop()
print(st)

print(st.peek())