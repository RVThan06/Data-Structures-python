"""Python implementation of singly linked list.

   In this linked list application, duplicates items are involved
   however, implementing list without duplicate items
   will allow for more efficient seraching and deletion
   as there will be no need to traverse whole list often.
"""

# standard library imports


class Node:
    """To create node."""

    def __init__(self, value: int) -> None:
        """Initialising node."""
        self.data = value
        self.next = None


    def __str__(self) -> str:
        return str(self.data)

class LinkedList:
    """To create singly linked list."""

    def __init__(self) -> None:
        """Initialise first node as None."""
        self.head = None


    def __str__(self) -> str:

        temp_node = self.head
        node_list = []

        if temp_node is None:
            return "Empty list"

        while temp_node is not None:
            node_list.append(str(temp_node.data))
            temp_node = temp_node.next

        node_list.append("None")
        return " --> ".join(node_list)


    def __iter__(self) -> Node:
        """Iterator to iterate list O(n)."""

        # each iteration yield a node in list
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def insert_front(self, value: int) -> None:
        """To isert data to head. O(1)"""

        new_node = Node(value=value)
        new_node.next = self.head
        self.head = new_node


    def insert_rear(self, value: int) -> None:
        """To insert data to rear using traversal. O(n)"""

        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            return

        # inseting to rear requires traversal till last node
        for current_node in self:
            pass
        # current node is the last node
        current_node.next = new_node


    def insert_before(self, value: int, target_node_data: int) -> None:
        """Insert data between nodes."""

        if self.head is None:
            return "The list is empty"

        # insert at front
        if self.head.data == target_node_data:
            self.insert_front(value=value)
            return

        prev_node = self.head
        # iterate through the node
        for node in self:

            # first if condition will be false since its head
            if node.data == target_node_data:
                new_node = Node(value=value)
                new_node.next = node
                prev_node.next = new_node
            # after first if statement prev_node is head
            prev_node = node


    def delete_node(self, target_node_data: int) -> None:
        """Delete target node based on value passed O(n)."""

        if self.head is None:
            return "List if empty"

        # first check if head matches then delete head
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        # first if condition will be false since its head is not target
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                # when deletion happens next prev node is still the same prev node
                # only when list has duplicate elements use continue
                continue
            prev_node = node


    def search_item(self, target_data: int) -> None:
        """Check target node if exist using linear search O(n)."""

        if self.head is None:
            return "List is empty"

        # use counter if there is duplicate data
        # we store index of duplicate data in list
        counter = 0
        pos_list = []
        for node in self:
            if node.data == target_data:
                pos_list.append(counter)
            counter += 1

        if pos_list:
            return f"Nodes detected at index {pos_list} ."


    def retrieve_data(self, item_position: int) -> None:
        """retreive data from given index using linear search O(n)."""

        if self.head is None:
            return "List is empty"

        counter = 0
        for node in self:
            if counter == item_position:
                return node.data
            counter += 1


    def sort_list(self):
        """Sort list in ascending order using bubble sort."""
        pass


# function calls
# instatiate linked_list object
linked_list =LinkedList()

# create nodes and store data
for i in range(6):
    linked_list.insert_rear(i)
print(linked_list)

# insert item using various methods
linked_list.insert_front(3)
linked_list.insert_rear(6)
linked_list.insert_before(value=4, target_node_data=5)
print(linked_list)

# delete node
linked_list.delete_node(4)
print(linked_list)

# search for all position of item 3 in list
print(linked_list.search_item(3))

# retreive item at index 4 which is "3"
print(linked_list.retrieve_data(4))

for i in range(5):
    linked_list.insert_front(1)

print(linked_list)
