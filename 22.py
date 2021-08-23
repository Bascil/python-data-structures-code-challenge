# Queue
'''
A queue is a first in first out (FIFO) data structure.
Enqueue - add an item to the end of the queue
Dequeue - remove an item from the front of the queue

Use Cases
Bank Tellers
Placing an order
Supermarket checkout
'''

# We can use append to enqueue an item and popleft to dequeue an item
# Deque is a double ended queue, but we can use it for a queue

from collections import deque

my_queue = deque()
my_queue.append(5)
my_queue.append(7)
my_queue.append(6)

print(my_queue)
print(my_queue.popleft())
print(my_queue.popleft())
print(my_queue.popleft())



 
