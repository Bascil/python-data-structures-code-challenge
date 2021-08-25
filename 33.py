# Doubly Linked List Implementation
# Node class
class Node:
  def __init__(self, d = None, n = None, p = None):
    self.data = d
    self.next_node = n
    self.prev_node = p
  
  def __str__(self):
    return ('(' + str(self.data) + ')')
  
class DoublyLinkedList:
  def __init__(self, r = None):
    self.root = r
    self.last = r
    self.size = 0
    
  def add(self, d):
    if self.size == 0:
      self.root = Node(d)
      self.last = self.root
    else:
      new_node = Node(d, self.root)
      self.root.prev_node = new_node
      self.root = new_node
      
    self.size +=1
    
  # similar to standard/singly linked list
  def find(self, d):
    this_node = self.root
    while this_node is not None:
      if this_node.data == d:
        return d
      elif this_node.next_node == None:
        return False
      else:
        this_node = this_node.next_node
        
  def remove(self, d):
    this_node = self.root
    while this_node is not None:
      if this_node.data == d:
        if this_node.prev_node is not None:
          if this_node.next_node is not None: # delete middle node
            this_node.prev_node.next_node = this_node.next_node
            this_node.next_node.prev_node = this_node.prev_node
          else: # delete last node
            this_node.prev_node.next_node = None
            self.lasst = this_node.prev_node
        else: # delete root node
          self.root =this_node.next_node
          this_node.next_node.prev_node = self.root
        self.size -=1
        return False
      else:
        this_node = this_node.next_node
    return False   
  
  def print_list(self):
    if self.root is None:
      return
    this_node = self.root  
    print(this_node, end = '->')  
    
    while this_node.next_node is not None:
      this_node = this_node.next_node
      print(this_node, end = '->')
    print()
    
# Test Code
dll = DoublyLinkedList()

for i  in [5,9,3,8,9]:
  dll.add(i)
  
print("Size " + str(dll.size)) # Size 5
dll.print_list() # (9)->(8)->(3)->(9)->(5)->
dll.remove(8)
print("Size " + str(dll.size))  # Size 4     
print(dll.remove(15)) # False
print(dll.find(15)) # False
dll.add(21)
dll.add(22)
dll.add(5)
dll.print_list() # (5)->(22)->(21)->(9)->(3)->(9)->(5)->

# Last node's previous node
print(dll.last.prev_node) # (9)


    