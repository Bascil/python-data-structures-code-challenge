# Graphs
'''
Perfect for modeling real world objects e.g social and computer networks

A graph consists of vertices and edges connecting these vertices. For example
in a social network, the vertices could be people and the connections(edges) could 
be friendships


Basil ------James              Tijani
  \        /  |   \          /
   \      /   |    \        /
     Lynn     |     \      /
     /        |     Swaleh
    /         |          \
   /          |           \
Lilian-------Martin       Julius    

Types of Graphs
(i)  Undirected graphs
     Relationship is bidirectional(2 way). Is the most common way
     to model relatioship in a social network  
     
(ii) Directed Graph
     Relatioships are one way. Used to model airplane flights and bus routes
     between cities. Each leg of the flight is represented by an arrow denoting direction
     
     If you have a flight going from chicago to seattle, it doesnt necessarily have a return flight
     
     Seattle            Detroit
      | \                 /\ \         
      |  \                  \ \       
      |   \                  \ \/
      |   Chicago   ---------> New York 
      |    /\     \ <--------  /\
      |   /        \             \
      |  /          \             \
     \| /            \             \
      Los Angeles     \         Miami
                       \        /\
                        \/     /
                       Atlanta
                      / /\     
                     / /
                   \/ /
                 Dallas      
      
  Applications
  - Transportation
  - Networking
  
      