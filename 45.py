# Code implementation using adjacency matrix
class Vertex:
  def __init__(self, n):
    self.name = n
    
class Graph:
  vertices = {}
  edges = []
  edge_indices = {}
  
  def add_vertex(self, vertex):
    # verify a valid vertex object and that the vertex is not in the list
    if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
      # update vertices dict by adding name and vertices to the dict
      self.vertices[vertex.name] = vertex
      
      # use a loop to append a column to the rightmost side of the matrix
      for row in self.edges:
        row.append(0)
        
      # append a row of zeros at the very bottom
      self.edges.append([0]* (len(self.edges) + 1))
      
      self.edge_indices[vertex.name] = len(self.edge_indices)
      
      return True
    else:
      return False
    
  def add_edge(self, u, v, weight=1):
    if u in self.vertices and v in self.vertices:
      self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
      self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
      return True
    else:
      return False
  
  def print_graph(self):
    for v, i in sorted(self.edge_indices.items()):
      print(v + ' ', end = ' ')
      
      for j in range(len(self.edges)):
        print(self.edges[i][j], end=' ')
      print(' ')
      
# Test code

# create a new graph object
g = Graph()

# create a new vertex named A
a = Vertex('A')

# add A to the graph
g.add_vertex(a)

# add a new vertex B to the graph
g.add_vertex(Vertex('B'))

# iterate from A to K and add vertices to the graph
for i in range(ord('A'), ord('K')): # ord - get numerical equivalent
  g.add_vertex(Vertex(chr(i)))
  
# an edge consists of two vertex names
edges = [ 'AB', 'AE', 'BF', 'CG', 'DE'
          'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ' ]

# we iterate through a list of edges and add each to the graph
for edge in edges:
  g.add_edge(edge[0], edge[1])
  
g.print_graph()