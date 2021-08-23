# Stack implementation
'''
Stack using python list. Use append to push an item
onto the stack and pop to remove an item 
'''

my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)

print(my_stack)
print(my_stack.pop()) # 19
print(my_stack.pop()) # 12
print(my_stack) # [4,7]
