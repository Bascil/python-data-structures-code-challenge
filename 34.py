# Trees
'''
You can locate data in a large tree with very few comparisons.

Each part of a tree is called a node, end each connection between 
nodes is called an edge. At the very top of the tree is the root node


          5 - (root/parent)
  (edge) /   \  
        3     8 (child/sibling)
       /  \   /  \
      1   4  6    9

Nodes of the same parent are called sibling nodes and the botton node 
is called the leaf node.

          3
         /  \
(leaf)  1    4

Leaf nodes are found at the bottom of the tree and have no children

BINARY TREE
In a binary tree, each node can have upto 2 child nodes. A subtree is a part of a tree
which in itself is a tree

                              5 
(3,5 are node 4's ancestors) /   \  
                            3     8 (8,6,9 form a subtree as well as 3,1,4)
                          /  \   /  \
                         1   4  6    9

3 and 5 are ancestors to node 4, node 5's descendants include everything 
in its left and right subtrees

Each node is greater than every node in its left subtree


                      15 
                     /   \  
                   8      24 
                  / \    / \
                 5  11 19  28
                / \   \     \
               2   6  13    25

8 is greater than every node in its left subtree, 5,2,6
24 is greater than every node in its left subtree