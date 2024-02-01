"""Linked list program for adjacency list integration."""


# standard library imports


class Node:
    """To create node."""

    def __init__(self, vertex: int) -> None:
        """Initialising node where each node is a vertex."""

        self.vertex = vertex
        self.next = None

    def __str__(self) -> str:
        return str(self.vertex)


class LinkedList:
    """To create singly linked list of vertices."""

    def __init__(self) -> None:
        """Initialise first node as None."""
        self.head = None


    def __str__(self) -> str:

        temp_node = self.head
        node_list = []

        if temp_node is None:
            return "Empty list"

        while temp_node is not None:
            node_list.append(str(temp_node.vertex))
            temp_node = temp_node.next

        node_list.append("None")
        return " --> ".join(node_list)


    def __iter__(self) -> Node:
        """Iterator to iterate list O(n) but in avarage case o(1)."""

        # each iteration yield a node in list
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def insert_front(self, vertex: int) -> None:
        """To isert data to head O(1)."""

        new_node = Node(vertex=vertex)
        new_node.next = self.head
        self.head = new_node


    def delete_node(self, target_node_vertex: int) -> None:
        """Delete target node based on key passed O(n)"""

        # first check if head matches then delete head
        if self.head.vertex == target_node_vertex:
            self.head = self.head.next
            return

        # then check the rest of the list
        prev_node = self.head
        # first if condition will be false since its head is not target
        for node in self:
            if node.vertex == target_node_vertex:
                prev_node.next = node.next
                return

            prev_node = node

        raise Exception("Edge does not exist")


    def search_node(self, target_vertex: int) -> bool:
        """Check target node if exist O(n)."""

        # if list is empty then no node/vertices are present
        if self.head is None:
            return False

        # check every node, if target vertex exist
        for node in self:
            if node.vertex == target_vertex:
                return True

        # if vertex didn't exist in linked list
        return False
