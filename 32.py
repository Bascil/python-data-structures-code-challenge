# Doubly LInked List
'''
Has a pointer to hte next and previous node and the data itself

                prev |  data  |  next
    <----------  .   |   23   |   .------------>
    
Every node has three parts, data and pointers to prevoius and next nodes

Simple Doubly Linked List with 3 Nodes

  prev |  data  |  next           prev | data | next       prev  data   next
     . |   23   |   .---->  ---->   .  |   23 |  .   ---->   .    7      .
                            <----                    <----
Advantages
You can Iterate through the list in either direction
You can delete a node without iterationg through the entire list, you can get the 
node on either side of the list