# Directed Graph
'''
A has an outbound edge to C. B connects to A, but A does not
connect directly to B

         B                   Adjacency List
       /  /\                 A: C
      /     \                B: A
    \/       \               C: B, D, E
    A -------> C             D: C
     /\       /  \           E: A
       \     /    \
        \  \/      \/
          E        D
          
            Adjacency Matrix

                    to

             A     B     C     D     E
            
        A    0     0     1     0     0
        
        B    1     0     0     0     0
from      
        C    0     1     0     1     1
          
        D    0     0     0     0     0
        
        E    1     0     0     0     0

          
