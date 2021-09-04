# BST Implementation
class Tree:
  # constructor sets three attrs data, left subtree and right subtree
  def __init__(self, data, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right
    
  # inserts a new subtreeinto the proper location
  def insert(self, data):
    if self.data == data:
      return False
    elif self.data > data:
      if self.left is not None:
        return self.left.insert(data)
      else:
        self.left = Tree(data)
        return True
    else:
      if self.right is not None:
        return self.right.insert(data)
      else:
        self.right = Tree(data)
        return True
      
  # finds a value, if not found return false
  def find(self, data):
    if self.data == data:
      return data
    elif self.data > data:
      if self.left is None:
        return False
      else:
        return self.left.find(data)
    elif self.data < data:
      if self.right is None:
        return False
      else:
        return self.right.find(data)   
  
  # returns the number of nodes in a tre
  def get_size(self):
    if self.left is not None and self.right is not None:
      return 1 + self.left.get_size() + self.right.get_size()
    elif self.left:
      return 1 + self.left.get_size()
    elif self.right:
      return 1 + self.right.get_size()
    else:
      return 1
      
  # prints a preorder traversal of the tree
  def preorder(self):
    # check if current node is not none
    if self is not None:
      print(self.data, end =' ')
      if self.left is not None:
        self.left.preorder()
      if self.right:
        self.right.preorder()
      
  # prints an inorder traversal of the tree
  def inorder(self):
    if self is not None:
      if self.left is not None:
        self.left.inorder()
      print(self.data, end = ' ')
      
      if self.right is not None:
        self.right.inorder()
        
# Test code
# create a new tree with 7 as root
tree = Tree(7)

# insert 9 to the tree
tree.insert(9)

for i in [15,10,2,12,3,1,13,6,11,4,14,9]:
  tree.insert(i)
  
for i in range(16):
  print(tree.find(i), end=' ')
  
print('\n', tree.get_size())

tree.preorder()
print()

tree.inorder()
print()


  
  
  
    
    
    