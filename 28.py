# Regular / Singly Linked List Implementation

# Node class
class Node:
  def __init__(self, d = None, n = None, p = None):
    self.data = d
    self.next_node = n
    self.prev_node = p
  
  def __str__(self):
    return ('(' + str(self.data) + ')')

class SinglyLinkedList:
  
  def __init__(self, r = None):
    self.root = r
    self.size = 0
    
  def add(self, d):
    new_node = Node(d, self.root)
    self.root = new_node
    self.size +=1
    
  def find(self, d):
    this_node = self.root
    while this_node is not None:
      if this_node.data == d:
        return d
      else:
        this_node == this_node.next_node
      return None
  
  def remove(self, d):
    this_node = self.root
    prev_node = None
    while this_node is not None:
      if this_node.data == d:
        if prev_node is not None:
          prev_node.next_node = this_node.next_node
        else:
          self.root = this_node.next_node
          self.size -=1
        return True
      else:
        prev_node = this_node
        this_node = this_node.next_node
        return False
        
  def print_list(self):
    this_node = self.root
    while this_node is not None:
      print(this_node, end = '->')
      this_node = this_node.next_node
    print('None')
          
# Test Code
myList = SinglyLinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list() 
# output (12)->(8)->(5)->None

print("Size " + str(myList.size))
# myList.remove(8)
# print("Size " + str(myList.size))  # Not working
print(myList.find(12))
print(myList.root) #(12)

      
      
  
  
  