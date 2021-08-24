# Circular Linked Lists
'''
Almost similar to standard/singly linked list except that fron the
very end, instead of having a None pointer at the end it will loop
back to the root node

9|next         12|next     15|.

/.\                         .
 ............................

When adding a new node, we do not insert the root node as the new node
anymore. We insert it as the second node(root next node)

add(8)
            8|next
            /\    .       
         .          .
      .              \/
9|next                12|next       15 |.

Advantage
Ideal for modelling continuously looping objects such as a monopoly
board or race track