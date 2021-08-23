# Max heap Operations
# Include push, peek and pop operations
'''
Push - push an item onto the heap
Peek - get max item in the heap
Pop - remove max item in the heap

Push 
Add a value to the end of the array and float
it up to its proper position(float up/ bubble up)

Example - Assume we wanted to push 12 onto the heap
--->12. We place it at the last spot in the array, i.e 11s right 
child and then float it to its proper position

                    11
                   /  \
                  5   12
                  
We then compare 12 to 11, if 12 is greater than 11, they will swap positions
                    
                    12
                   /  \
                  5   11
                
We then compare 12 to its new parent 16, check if 12 is greater than 16, so
there is no more swapping

Peek
Return the value at the top of the heap ie 25

Pop
Move the max to the end of the array, swap 25 with 11

           11 
         /   \  
        16     24
       /  \   /  \
      5   12 19   1
     / \  / \
    2  3  5  25
    
Delete 25 from the heap
         11 
         /  \  
        16   24
       /  \   / \
      5   12 19   1
     / \  / 
    2  3  5  
  
Bubble down the item at the first index (11) to its proper position i.e
Compare 11 to 24 so it moves down

          24
         /  \  
        16   11
       /  \   / \
      5   12 19   1
     / \  / 
    2  3  5  
  
Compare 11 to 19, 11 is less than 19 so it moves down(swap places)  
          
          24
         /  \  
        16   19
       /  \   / \
      5   12 11   1
     / \  / 
    2  3  5            
   W               