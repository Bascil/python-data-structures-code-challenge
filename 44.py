# Graph implementation using adjacency matrix
'''
Vertex class
A vertex class only needs to store its name
'''
class Vertex:
  def __init__(self, n):
    self.name = name
    
'''
Graph class
Has 3 attributes
1. vertices
  A dictionary with vertex_name, vertex_object

2. edges
  2D list i.e matrix of edges. For an unweigghted graph
  it will contain 0 for no ege and 1 for edges
  
3. edge_indices
   a dictionary with vertex_name:list_index e.g A:0 to access
   edges
   
Methods
add_vertex
updates all three of these attributes

add_edge
only needs to update the edges matrix




    