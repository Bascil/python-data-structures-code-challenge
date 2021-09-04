# Weighted Edges
'''
Much easier to represent compared to adjacency matrix. Used
to represent distance and time between nodes

          B                 
        /   \                
     8 /     \ 5          
      /   9   \              
    A -------- C            
     \       /  \           
   6  \   1 /    \ 3
       \   /      \
         E         D
          
          Adjecency Matrix
          
                    to

             A     B     C     D     E
            
        A    0     8     9     0     6
        
        B    8     0     5     0     0
from      
        C    9     5     0     3     1
          
        D    0     0     3     0     0
        
        E    6     0     1     0     0
