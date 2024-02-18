"""Implemnetatio of max heap data structure in python."""


# standard library imports
import math as mt


class MaxHeap:
    """TO create a heap."""

    def __init__(self) -> None:

        self.my_heap = []


    def __str__(self) -> str:
        """To print the heap"""

        return "-->".join(str(val) for val in self.my_heap)


    def insert_node(self, value:int) -> None:
        """To insert value into heap."""

        self.my_heap.append(value)


    def heapify_tree(self) -> None:
        """Heappify the entire heap."""

        # find the internal nodes(non-leaf nodes)
        nodes = mt.floor(len(self.my_heap)/2) - 1

        # heapify each internal node from deepest internal node to root node
        # this ensures as we reach higher internal nodes the left and right subtree is a heap
        for index in range(nodes, -1, -1):
            self.heapify(index)


    def delete_node(self, value: int) -> None:
        """To delete a node for a given value."""

        if value == self.my_heap[-1]:
            self.my_heap.pop()
            return

        index = self.my_heap.index(value)
        last_index = len(self.my_heap) - 1

        # swap node to be deleted with last node
        self.my_heap[index] = self.my_heap[last_index]
        # remove last node, so value deleted
        self.my_heap.pop()
        # heapify from the deleted index
        self.heapify(index=index)


    def heapify(self, index:int) -> None:
        """Heapify from parent(deleted node) to child."""

        # compare parent node with the child nodes till leaf
        length = len(self.my_heap)
        largest = index
        left_child = 2*index + 1
        right_child = 2*index + 2

        # run algo as long as child nodes exist, find the largest child
        if right_child < length and self.my_heap[right_child] > self.my_heap[index]:
            largest = right_child

        if left_child < length and self.my_heap[left_child] > self.my_heap[largest]:
            largest = left_child

        # swap parent with child if child is larger
        if largest != index:
            temp = self.my_heap[index]
            self.my_heap[index] = self.my_heap[largest]
            self.my_heap[largest] = temp
            # next recursion move to child node just swaped, so we go to lower nodes to heapify
            self.heapify(largest)


# function calls

# 1. Add elements to a list
new_heap = MaxHeap()
insertion_values = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
for val in insertion_values:
    new_heap.insert_node(val)

# 2. Heapify the list to create heap
new_heap.heapify_tree()
print(new_heap)

# 3. delete items in heap and heapify everytime an element is deleted
new_heap.delete_node(14)
print(new_heap)

new_heap.delete_node(42)
print(new_heap)

new_heap.delete_node(44)
print(new_heap)

new_heap.delete_node(35)
print(new_heap)

new_heap.delete_node(31)
print(new_heap)
