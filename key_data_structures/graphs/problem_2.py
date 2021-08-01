'''
Implementation of an undirected graphs with mutual relationships in Python
Using a breadth first traversal to visit each vertex in the graph

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

def bfs_traverse(vert):
    # This is used to keep track of each vertex which needs to be visited
    queue = []

    # This hash table keeps track of each visited vertex
    visited_vertices = {}

    visited_vertices[vert.value] = True
    queue.append(vert)

    while len(queue) > 0:
        current_vert = queue.pop(0)

        print(current_vert.value)

        for i in range(len(current_vert.adjacent_vertices)):
            # Check if the vertex has already been visited or not
            if current_vert.adjacent_vertices[i].value in visited_vertices:
                continue
            else:
                visited_vertices[current_vert.adjacent_vertices[i].value] = True
                queue.append(current_vert.adjacent_vertices[i])

print('Visiting and printing each vertex value using breadth first search')
bfs_traverse(alice_vert)

