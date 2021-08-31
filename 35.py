# Binary Search Tree (BST) Operations
# a. Insert - add new data in the tree
# b. Find  - locate data in the tree
# c. Delete - remove a node from the tree
# d. get_size - count number of nodes in the tree
# e. Traverse - walk through the tree node by node

'''
Tree Example

                      15 
                     /   \  
                   8      24 
                  / \    / \
                 5  11 19  28
                / \   \     \
               2   6  13    25
a. BST Insert
Start at root 15. To insert 12, 
- Check if 12 < 15, yes, descend to 15's left subtree
- Check if 12 < 8, no, descend on 8's right subtree
- Check if 12 < 11, no, descend down the tree
- Check if 12 < 13, yes, add it as 13's left child

          13
          /
         12

b. BST Find
Start at root 15. To find 19,
- Is 19 < 15, no, descend down to 15's right subtree
- Is 19 < 24, yes, descend to 24's left subtree

                15
                  \
                  24
                  /  \
          here - 19    28
          
c. BST Delete
3 different possibilities;
- The node we want to delete is a leaf node
- It has 1 child nodes
- It has two child nodes

In case the number we want to delete is a leaf node 
e.g 2, 6, 12, 19 and 25, its easy for us to just delete the leaf
node without affecting anything else in the tree. Its the easiest case

In the case of 1 child, promote the child to the target nodes position
if we wanted to delete 28, we would promote 25 to 28's position. If we wanted 
to delete 11, we would promote 13 to 11's position

If you have two children,say you wanted to delete 24, you notice 24 has 2 children,
descend down 24s right subtree and then all the way to the left, to get to 25, 
so you basically swap places, between the 24 and 25 and then delete the 24. 
So you place the 25 where the 24 was.

If you wanted to delete 4, notice that 4 has two children, find the next higher node after
4, that is 6, then descend down, we then delete the 4 and promote the 6 to the 4s position

d. Get Size
Its a pretty easy operation. It works by using recursion. Size of the 3's subtree is
size = 1 + size of 3's left subtree + size of 3's right subtree. We call recursively, the get_size
function as we descend down the tree, till we get to the leaf node and return a 1

e. Traversal 
To traverse data in a tree, there are different traversal algorithms;

Preoder traversal - visit the root before we visit the root's subtrees. 
We will start at the root and then visit the roots subtree. Start at the top, then
descend down to the left subtree and then still descend down the left subtree, then decsend
back up to 5s right subtree

                      5 
                     /   \  
                   3      8
                  / \    / \
                 1  4   6   9
                 
              1   2   3   4   5   6    7           
              5   3   1   4   8   6    9
              
Inoder traversal - visit the root between visiting the roots subtrees hence 
you can deliver values in sorted order. Start with the botton left most node
then walk or way up. 


                      5 
                     /   \  
                   3      8
                  / \    / \
                 1  4   6   9
                 
              1   2   3   4   5   6    7           
              1   3   4   5   6   8    9
              
Advantages of BSTs
i. Use recursion making then easy to implement
ii. Speed - fast at locating data. You can insert, find and delete data really fast.
    A balanced BST with 10,000,000 nodes can take upto 30 comparisons only
   



   
