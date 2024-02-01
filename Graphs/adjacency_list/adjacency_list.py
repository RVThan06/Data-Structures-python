"""Python program demonstrating adjancency list implemnentaion of
    graph data structure. Each array element represents a vertex and
    it stores a linked list containing all other vertices that forms edges with the given
    vertex.

    This is an undirected graph implementation.
"""

# standard library import

# local library imports
import linked_list as link


class AdjacencyList:
    """Class for creating adjacency list."""

    def __init__(self, size:int) -> None:
        """To initialise list objects."""

        self.size = size
        self.array = [None] * size


    def add_edge(self, vertex_1:int, vertex_2:int) -> None:
        """To add edges between vertices. O(1)"""

        # check if row & col is the same
        if vertex_1==vertex_2:
            raise Exception("vertices valuea are same.")

        if self.array[vertex_1] is None:
            new_list  = link.LinkedList()
            self.array[vertex_1] = new_list

        if self.array[vertex_2] is None:
            new_list  = link.LinkedList()
            self.array[vertex_2] = new_list

        self.array[vertex_1].insert_front(vertex_2)
        self.array[vertex_2].insert_front(vertex_1)


    def remove_edge(self, vertex_1:int, vertex_2:int) -> None:
        """To remove and edge between given vertices."""

        # check if row & col is the same
        if vertex_1==vertex_2:
            raise Exception("vertices valuea are same.")

        # remove the edge from both list
        self.array[vertex_1].delete_node(vertex_2)
        self.array[vertex_2].delete_node(vertex_1)


    def check_edge(self, vertex_1:int, vertex_2:int) -> bool:
        """To check an edge exist. O(n)"""

        status = self.array[vertex_1].search_node(vertex_2)
        return status


    def find_adjacent(self, vertex_1:int) -> list:
        """To find all adjacent vertices and return it
           in a list. O(n)
        """

        adj_list = []
        for vert in self.array[vertex_1]:
            if vertex_1:
                adj_list.append(vert.vertex)

        return adj_list


    def print_list(self) -> None:
        """To print entire list."""

        for links in self.array:
            print(links)
        print()


# main program

# 1. initialise graph
graph = AdjacencyList(6)

# 2. add edges
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(3, 1)
graph.add_edge(2, 4)
graph.add_edge(3, 2)

# 3. print the entire
graph.print_list()

# 4. find adjacent to vertice 1
print("adjacent to vertices 1 is :" + str(graph.find_adjacent(1)))
print()

# 5. delete edges
graph.remove_edge(1, 2)
graph.remove_edge(3, 1)
graph.print_list()

# 6. check exceptuion when removing edge that doesn't exist
try:
    graph.remove_edge(3, 1)
except Exception as err:
    print("Error: ", err)

# 7. check if edge exist between two vertices
print(graph.check_edge(2, 4), "\n")
