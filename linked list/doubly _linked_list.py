"""Program implementing doubly linked list"""

# standard library imports


class  Node:
    """To create node object."""

    def __init__(self, value: int) -> None:
        """To initialise node values."""

        self.data = value
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    """To create doubly linked list."""

    def __init__(self) -> None:
        """To initialise linked list."""

        self.head = None
        self.tail = None

    def __str__(self) -> str:
        """To allow printing of list data."""

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
        """Iterator to iterate list O(1)."""

        # each iteration yield a node in list
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert_front(self, value : int) -> None:
        """To insert node at front of list O(1)."""

        new_node = Node(value=value)

        # to insert first node to empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_rear(self, value: int) -> None:
        """To insert node to end of list O(1)."""

        if self.head is None:
            self.insert_front(value=value)
            return

        new_node = Node(value=value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_before(self, new_value: int, index: int) -> None:
        """To insert node in between list O(n)."""

        if self.head is None:
            # raise exception
            return

        # insert at front
        if index == 0:
            self.insert_front(value=new_value)
            return

        counter = 0
        for node in self:

            # insert new node at the desired index
            if counter == index:
                new_node = Node(value=new_value)
                new_node.prev = node.prev
                new_node.next = node
                node.prev.next = new_node
                node.prev = new_node
                return

            counter = counter + 1

    def delete_front(self):
        """To delete node at head O(1)."""

        if self.head is None:
            # raise an exception
            return "List is empty"

        # if head is the only node
        if self.head.next is None:
            self.head = None
            return

        new_head = self.head.next
        new_head.prev = None
        self.head = new_head

    def delete_rear(self):
        """To delete node at tail O(1)."""

        if self.head is None:
            return "List is empty"

        # if tail is the last node
        if self.tail.prev is None:
            self.delete_front()
            return

        new_tail = self.tail.prev
        new_tail.next = None
        self.tail = new_tail

    def delete_before(self, index: int):
        """To delete node before given index O(n)."""

        # check for empty list
        if self.head is None:
            return "List is empty"

        # if index is 0
        if index == 0:
            return "Cannot delete before head"

        if index == 1:
            if self.head.next is not None:
                self.delete_front()
                return
            else:
                return "Index not present"

        counter = 0
        not_present = True

        for node in self:
            if counter == index:
                temp_node = node.prev
                node.prev = temp_node.prev
                temp_node.prev.next = node
                not_present = False
            counter += 1

        if not_present:
            return "Index not in list"

    def search(self, value: int) -> Node:
        """To search for node with given value O(n)."""

        if self.head is None:
            return

        # return the node with required value
        for node in self:
            if node.data == value:
                return node


# function calls

linked_list = LinkedList()

# insert from rear
for i in range(5):
    linked_list.insert_rear(i)

print(f"After rear insertion \n{linked_list}")

# insert from front
for i in range(10,15):
    linked_list.insert_front(i)

print(f"After front insertion \n{linked_list}")

# insert in between list nodes
for i in range(5):
    linked_list.insert_before(new_value=1, index=4)

print(f"After in between insertion \n{linked_list}")

# to delete nodes from front
for i in range(3):
    linked_list.delete_front()

print(f"After front deletion\n{linked_list}")

# to delete nodes from rear
for i in range(3):
    linked_list.delete_rear()
print(f"After rear deletion \n{linked_list}")

# to delete before
linked_list.delete_before(5)
print(linked_list)

linked_list.delete_before(1)  # delete head
print(linked_list)

print(linked_list.delete_before(0))  # delete before head impossible

# to search for node with required data

found_node = linked_list.search(10)

if found_node:
    print(found_node.data)
else:
    print("Node not found")
