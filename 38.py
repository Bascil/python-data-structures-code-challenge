# Implementing Graphs - Adjacency List vs Adjacency Matrix
'''
Adjacency List
Stores a list of neighbours for each vertex in the vertex itself

Adjacency Matrix
Stores a 2D array of all the connections between the vertices and the 
graph object

Illustration
Consider an undirected graph with 5 vertices and a number of edges connecting them

          B                   Adjacency List
        /   \                 A: B, C, E
       /     \                B: A, C
      /       \               C: A, B, D, E
    A -------- C              D: C
     \       /  \             E: A,C
      \     /    \
       \   /      \
         E         D
          
Node A is connected to B, C and E, stored in node A's neighbour list
Node B is connected to A and C and stored in node B's list of neighbours

Adjacency Matrix
It has all the from vertices. It indicates 0 where there is no edge and 1 
where there is an edge

                    to

             A     B     C     D     E
            
        A    0     1     1     0     1
        
        B    1     0     1     0     0
from      
        C    1     1     0     1     1
          
        D    0     0     1     0     0
        
        E    1     0     1     0     0
