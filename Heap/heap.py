"""Implemnetatio  of heap data structure in python."""


# standard library imports
import math as mt


class MaxHeap:
    """TO create a heap."""

    def __init__(self) -> None:

        self.my_heap = []


    def __str__(self) -> str:
        """To print the heap"""

        return "-->".join(str(val) for val in self.my_heap)


    def insert_value(self, value:int) -> None:
        """To insert value into heap."""

        self.my_heap.append(value)
        index = len(self.my_heap) - 1  # index of latest element
        self.heapify(index=index)


    def heapify(self, index:int) -> None:
        """To heapify the heap."""

        while index:
            parent_index = mt.ceil(index/2) - 1
            # swap if the parent is smaller than child
            if self.my_heap[index] > self.my_heap[parent_index]:
                temp_value = self.my_heap[parent_index]
                self.my_heap[parent_index] = self.my_heap[index]
                self.my_heap[index] = temp_value
                index = parent_index
            else:
                break  # if parent is greater, then max heap is preserved


# function calls

new_heap = MaxHeap()
insertion_values = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
for val in insertion_values:
    new_heap.insert_value(val)
print(new_heap)
