# STACKS, QUEUES & HEAPS
# Stacks
'''
A stack is a last in first out (LIFO) data structure.
 - Push an item onto the stack
 - Pop an item out of the stack
 
All push and pop operations are to/from the top of the stack.
The only way to access the bottom items in the stack is to 
first remove all items above it

Peek - getting an item on top of the stack without removing it
Clear - clear all items from the stack

Use Cases
Undo - tracks which commands have been executed. Pop the last 
command off the command stack to undo it e.g pop the last command 
to undo bold. The program has to keep track of which command you
have executed in which order. 

Each time you execute a common, it pushes that command onto the stack
so that it has a record of it. If you hit the undo button, it will pop
the last command off the stack and reverse that command
'''

