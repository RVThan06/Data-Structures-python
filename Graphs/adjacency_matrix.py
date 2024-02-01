"""pyton program of graph data structure implementatiion
    using adjacency matrix.

    This is an undirected graph implementation.
"""

# standard library import

# local library imports


class AjacencyMatrix:
    """Class for 2d adjacency matrix."""

    def __init__(self, size:int) -> None:
        """Initialise the 2D matrix."""

        self.matrix = [[0 for i in range(size)] for j in range(size)]
        self.size = size


    def add_edge(self, row:int, col:int) -> None:
        """To add an edge to the matrix at [row, col]. O(1)"""

        # check if row & col is the same
        if row==col:
            raise Exception("Row and column value is same.")

        # set diagonal cells to 1
        self.matrix[row][col] = 1
        self.matrix[col][row] = 1


    def remove_edge(self, row:int, col:int) -> None:
        """To remove an edge from 2D matrix. O(1)"""

        # check if row & col is the same
        if row==col:
            raise Exception("Row and column value is same.")

        # set diagonal cells to 0
        self.matrix[row][col] = 0
        self.matrix[col][row] = 0


    def check_edge(self, row:int, col:int) -> bool:
        """To check an edge exist. O(1)"""

        status = False

        if self.matrix[row][col] == 1:
            status = True
        return status


    def find_adjacent(self, vertice:int) -> list:
        """To find all adjacent vertices and return it
           in a list. O(n)
        """

        adj_list = []
        adj_index = 0
        for cols in self.matrix[vertice]:
            if cols == 1:
                adj_list.append(adj_index)
            adj_index = adj_index + 1

        return adj_list


    def print_matrix(self) -> None:
        """To print matrix."""

        for rows in self.matrix:
            for col in rows:
                print(col, end="")
            print()
        print()


# main code

# graph instantiated
graph = AjacencyMatrix(6)  # 6 vertices

# add edges
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(3, 1)
graph.add_edge(2, 4)
graph.add_edge(3, 2)

# print the entire
graph.print_matrix()

# find adjacent to vertice 1
print("adjacent to vertices 1 is :" + str(graph.find_adjacent(1)))
print()

# check if edge exist between two vertices
print(graph.check_edge(1, 2), "\n")

# delete edges
graph.remove_edge(1, 2)
graph.remove_edge(3, 1)
graph.print_matrix()

# raise exception
try:
    graph.add_edge(2, 2)
except Exception as err:
    print("Error:", err)
