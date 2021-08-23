# Wrapper class implementation
from collections import deque

class Queue():
  def __init__(self):
    self.queue = deque()
    
  def enqueue(self, item):
    self.queue.append(item)
    
  def dequeue(self):
    if len(self.queue) > 0:
      return self.queue.popleft()
    else:
      return None
    
  def __str__(self):
    return str(self.queue)
  
# Test code
my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(7)
my_queue.enqueue(6)

print(my_queue)
print(my_queue.dequeue()) # 5
print(my_queue.dequeue()) # 7
print(my_queue.dequeue()) # 6
print(my_queue.dequeue()) # None

    