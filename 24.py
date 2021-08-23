
# Binary Heap
# A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, 
# the key at root must be minimum among all keys present in Binary Heap. 
# The same property must be recursively true for all nodes in Binary Tree

# Examples of Min Heap:
'''
          10                      10
         /      \               /       \  
       20        100          15         30  
      /                      /  \        /  \
    30                     40    50    100   40
'''
# How is Binary Heap represented?
# A binary heap is typically represented as an array. 
# The root element will be at Arr[0].


# Max heap
# A max heap is a complete binary tree in which  every node in the tree 
# is less than or equal to its parent.

# Use Cases - implementation of priority queue, heap sort, e.t.c

# Heaps are fast (O(log n)) and are easy to implement in python using a list
'''

          25 - (parent) - head
         /   \  
   (LC) 16     24 (RC)
       /  \   /  \
      5   11 19   1
     / \  /
    2  3  5

We will label our tree with indices 1 - 10

1   2   3   4   5   6   7  8  9  10
25  16  24  5   11  19  1  2  3   5

25 has to be greater than everything below it in the tree hence a max heap. 
Same applies to 24. We can now instantly access any node in the tree

Assume we wanted to access the value 5 whose index is 4 i.e i = 4
We can access 5s parent by simply deviding the index by 2

parent(i) = i/2

To access 5's children, 5's left child is i*2 and RC is (i*2) + 1

left(i) = i * 2  = 8
right(i) = (i * 2) + 1 = 9
