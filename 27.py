# Regular / Singly Linked List

'''
Every linked list is composed of nodes. Every node has two parts, data
and a pointer to the next node. The first node is called the root node
        ---------------
        data  | next
         17   |  .------>
        ----------------
Example
Each node has its own piece of data and a pointer to the next node
 ---------------     --------------       -------------
  data | next        data   |  next        data  |  next
    5  |  .------>    17    |  .------>      8   |   .
 ----------------    ---------------      ---------------
 
 Attributes
 root - pointer to the begining of the list
 size - number of nodes in the list
 
 operations
 find(data) - find data
 add(data)  - add a piece of data
 remove(data) - remove data from the list
 print_list()
 
 
 Example
 add(10)
 - Create a new node with data set as 10
   -----------------
      data  |  next
      10    |    .
   ------------------
 - Set the next pointer to point to the root
   
                -----------------
                    data  |  next
                    10    |    .
                ------------------
                    .
                  .
                \/
         -----------------          ----------------
            data  |  next             data  |   next
            5     |    . -------->     17   |    . ---------->
          ------------------        ----------------
          
- Insert 10 to the begining of the list and remove 5

    -----------------          ----------------
      data  |  next             data  |   next
        10  |    . -------->     17   |    . ---------->
    ------------------         -----------------
          