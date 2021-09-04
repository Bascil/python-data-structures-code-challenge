# Which is Better?

'''
Dense Graph
There are a number of edges relative to the number of 
vertices. If each vertex could be connected to every other vertex
then 
    number of edges = vertices^2(squared)
    
    graph where |E| = |V|^2
    
        o ------- o 
      /  \      /  \
     /    \    /    \
    o------\--/-----o
    |       \/      |
    o-------/\------o
     \     /  \     /
      \   /    \   /
       \ /      \ /
        o--------o
        
Sparse Graph
There are relatively fewer edges almost similar to the number
of vertices
graph where |E| = |V|

        o        o 
         \      /  
          \    /    
    o------\--/-----o
    |       \/      
    o       /\      o
           /  \     
          /    \   
         /      \ 
        o--------o

More
Adjacency matrix takes up |V|^2 space regardless of how
dense the graph is. Matrix for a graph with 10,000 vertices
will take up at least 100,000,000 bytes

Pros and Cons
Adjacency List
Pro - faster and uses less space for sparse graphs
Con - slower for dense graphs

Adjacency Matrix
Pros - faster for dense graphs
     - simpler for weighted edges
     
Con - uses more space
'''
     

