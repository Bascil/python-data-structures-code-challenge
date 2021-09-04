# Classes - Graph classes
'''
Graph class
Uses a distionary to store vertices in the format vertex_name
and vertex_object

To add a new vertex to the graph, we first check if the object 
passed in is a vertex object, then ckeck if it already exists 
in the graph. If both checks pass, then we add the vertex to the graph's vertices
dictionary. 

When we add an edge, we receive two vertex names, we first check if both vertex
names are valid, then we add each to the set

To print the graph, we iterate through the vertices and print each vertex 
name(the key) followed by the neighbours list

'''
class Graph:
  vertices = {}
  
  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
      self.vertices[vertex.name] = vertex
      return True
    else:
      return False
    
  def add_edge(self, u, v):
    if u in self.vertices and v in self.vertices:
      self.vertices[u].add_neighbours(v)
      self.vertices[v].add_neighbours(u)
      return True
    else:
      return False
  def print_graph(self):
    for key in sorted(list(self.vertices.keys())):
      print(key,sorted(list(self.vertices[key].neighbours)))

class Vertex:
  def __init__(self, n):
    self.name = n
    self.neighbours = set()
  
  def add_neighbours(self, v):
    self.neighbours.add(v)
    
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
  
edges = [ 'AB', 'AE', 'BF', 'CG', 'DE'
          'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ' ]

for edge in edges:
  g.add_edge(edge[0], edge[1])
  
g.print_graph()

        
      