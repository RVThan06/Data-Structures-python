"""Linked list program for hash table integration."""


# standard library imports


class Node:
    """To create node."""

    def __init__(self, key: str, value: int) -> None:
        """Initialising node."""
        self.key = key
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
        """Iterator to iterate list O(n) but in avarage case o(1)."""

        # each iteration yield a node in list
        node = self.head
        while node is not None:
            yield node
            node = node.next


    def insert_front(self, key: str, value: int) -> tuple:
        """To isert data to head O(1) assuming searching is O(1)."""

        # search if key already present
        key_status = self.search_item(target_key=key)

        # Only add new node when key is absent in list
        if not key_status[0]:
            new_node = Node(key=key, value=value)
            new_node.next = self.head
            self.head = new_node

        # return key status display whether key was added or not
        return key_status


    def delete_node(self, target_node_key: str) -> tuple:
        """Delete target node based on key passed O(1) assuming uniform hashing."""

        # # search if key already present
        # key_status = self.search_item(target_key=target_node_key)

        # # Only delete node when key is present in list
        # if key_status[0]:

        # first check if head matches then delete head
        if self.head.key == target_node_key:
            self.head = self.head.next
            return (True, "Key present")

        prev_node = self.head
        # first if condition will be false since its head is not target
        for node in self:
            if node.key == target_node_key:
                prev_node.next = node.next
                return (True, "Key present")

            prev_node = node

        return (False, "Key error")


    def search_item(self, target_key: str) -> tuple:
        """Check target node if exist based on our assumption in average case : O(1)."""

        if self.head is None:
            return (False, "Key error")

        for node in self:
            if node.key == target_key:
                return (True, f"Key: '{node.key}' present")

        return (False, "Key error")
