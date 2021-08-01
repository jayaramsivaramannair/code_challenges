'''
Implementation of an undirected graphs with mutual relationships in Python
Using a depth first traversal to visit each vertex in the graph

'''

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertices(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertices(self)


# This will build out the entire graph
alice_vert = Vertex('Alice')
bob_vert = Vertex('Bob')
candy_vert = Vertex('Candy')
derek_vert = Vertex('Derek')
elaine_vert = Vertex('Elaine')
fred_vert = Vertex('Fred')
helen_vert = Vertex('Helen')
gina_vert = Vertex('Gina')
irena_vert = Vertex('Irena')

alice_vert.add_adjacent_vertices(bob_vert)
alice_vert.add_adjacent_vertices(candy_vert)
alice_vert.add_adjacent_vertices(derek_vert)
alice_vert.add_adjacent_vertices(elaine_vert)

bob_vert.add_adjacent_vertices(fred_vert)

fred_vert.add_adjacent_vertices(helen_vert)

helen_vert.add_adjacent_vertices(candy_vert)

derek_vert.add_adjacent_vertices(elaine_vert)
derek_vert.add_adjacent_vertices(gina_vert)

irena_vert.add_adjacent_vertices(gina_vert)

#Traversing the graph using Depth First Search. This involves recursive call on each vert
def dfs_traversal(vert, visited_vertices):
    visited_vertices[vert.value] = True

    print(vert.value)

    for i in range(len(vert.adjacent_vertices)):
        # check if the vert has already been visited
        if vert.adjacent_vertices[i].value in visited_vertices:
            continue
        else:
            dfs_traversal(vert.adjacent_vertices[i], visited_vertices)

#Searching the graph for a particular value using depth first traversal
def dfs_search(vert, search_value, visited_vertices):
    if vert.value == search_value:
        return vert.value

    visited_vertices[vert.value] = True

    for i in range(len(vert.adjacent_vertices)):
        if vert.adjacent_vertices[i].value == search_value:
            return vert.adjacent_vertices[i].value

        if vert.adjacent_vertices[i].value in visited_vertices:
            continue
        else:
            dfs_search(vert.adjacent_vertices[i], search_value, visited_vertices)
        
    #If the search value cannot be found
    return search_value + ' is not contained in this graph'


#This hash table keeps track of all visited vertices
visited_vertices = {}
#This traversal will visit each vertex which has not been visited yet and prints their value
dfs_traversal(alice_vert, visited_vertices)

search_table = {}
print('Printing result of the searching the graph:')
print(dfs_search(alice_vert, 'Derek', search_table))

