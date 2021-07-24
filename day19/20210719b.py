'''
You are given a directed acyclic graph (DAG) that contains N nodes.

Write a function that can find all the possible paths from node 0 to node N - 1

graph[a] is a list of all nodes b for which the edge a -> b exists. 

Example:

Input: graph = [[1, 2],[3],[3],[4],[]]
Output: [[0,1,3,4], [0,2,3,4]]


source: codesignal.com (Lambda Challenge)
source: How to sort a list of lists (https://www.pythonpool.com/python-sort-list-of-lists/)
'''

def csFindAllPathsFromAToB(graph):
    graph_list = { }
    for i in range(len(graph)):
        graph_list[i] = graph[i]

    paths = []

    def pre_order_traversal(start_vertex, graph, current_path):
        current_path.append(start_vertex)
        # Check all the neighbors for the start_vertex
        neighbors = graph[start_vertex]
        if (len(neighbors) == 0):
            paths.append(current_path)

        for neighbor in neighbors:
            pre_order_traversal(neighbor, graph, current_path.copy())

    pre_order_traversal(0, graph_list, [])

    paths.sort(reverse=False)

    return paths

print(csFindAllPathsFromAToB([[1, 2],[3],[3],[4],[]]))
print(csFindAllPathsFromAToB([[1,2], [3], [3], []]))
print(csFindAllPathsFromAToB([[4,3,1], [3,2,4], [3], [4], []]))
print(csFindAllPathsFromAToB([[1], []]))
