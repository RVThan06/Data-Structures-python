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
        index = len(self.my_heap) - 1  # index of latest element
        self.heapify(index=index)


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
        self.heapify_delete(index=index)
        return

    # this function is flawed, fix it
    def heapify(self, index:int) -> None:
        """To heapify the heap when building heap."""

        # everytime heapify the whole tree
        while index:
            parent_index = mt.ceil(index/2) - 1

            # swap if the parent is smaller than child
            if self.my_heap[index] > self.my_heap[parent_index]:
                temp_value = self.my_heap[parent_index]
                self.my_heap[parent_index] = self.my_heap[index]
                self.my_heap[index] = temp_value

            index = parent_index


    def heapify_delete(self, index:int) -> None:
        """Heapify from parent to child."""

        length = len(self.my_heap)
        largest = index
        left_child = 2*index + 1
        right_child = 2*index + 2

        if left_child < length and right_child < length:
            larger_child = left_child
            if self.my_heap[right_child] > self.my_heap[left_child]:
                larger_child = right_child

            if self.my_heap[larger_child] > self.my_heap[index]:
                largest = larger_child

            if largest != index:
                temp = self.my_heap[index]
                self.my_heap[index] = self.my_heap[largest]
                self.my_heap[largest] = temp
                self.heapify_delete(largest)





# function calls

# 1. crreate heap and add elements
new_heap = MaxHeap()
insertion_values = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]

# 2. print the heap
for val in insertion_values:
    new_heap.insert_node(val)
print(new_heap)

# 3. delete items in heap
new_heap.delete_node(14)
print(new_heap)

new_heap.delete_node(42)
print(new_heap)

new_heap.delete_node(44)
print(new_heap)

new_heap.delete_node(35)
print(new_heap)

new_heap.insert_node(12)
print(new_heap)

new_heap.insert_node(40)
print(new_heap)
