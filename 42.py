# Classes - Vertex and Graph classes
'''
Vertex class
Has a constructor that sets the name of the vertex
and creates a new empty set to store neighbours

The add neighbour method adds the name of a neighbouring
vertex to the neighbours set. This set automatically eliminates
duplicates. If a neighbour is already created, it cannot be added
'''

class Vertex:
  def __init__(self, n):
    self.name = n
    self.neighbours = set()
  
  def add_neighbours(self, v):
    self.neighbours.add(v)

