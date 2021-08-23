# Stack using a List with a wrapper class
class Stack():
  def __init__(self):
    self.stack = list()
  
  def push(self, item):
    self.stack.append(item)
    
  def pop(self):
    if len(self.stack) > 0:
      return self.stack.pop()
    else:
      return None
    
  def peek(self):
    if len(self.stack):
      return self.stack[len(self.stack) - 1]
    else:
      return None
    
  def __str__(self):
    return str(self.stack)
  
# Test Code
my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(5)
my_stack.push(7)

print(my_stack)  # [1, 3, 5, 7]

print(my_stack.pop()) # 7
print(my_stack.peek()) # 5
print(my_stack.pop()) # 5
print(my_stack.pop()) # 3
print(my_stack.pop()) # 1
print(my_stack.pop()) # None

    
