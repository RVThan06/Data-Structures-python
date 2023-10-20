"""Program to implement binary search tree."""

# standard library imports


class Node:
    """To create nodes."""

    def __init__(self, value: int) -> None:

        self.key = value
        self.right = None
        self.left = None


class BinarySearchTree:
    """To create a binary search tree."""

    def __init__(self, key) -> None:

        self.root = Node(value=key)


    def iterative_insert(self, value: int) -> None:
        """Node insertion using while loop."""

        direction = 0
        node = self.root

        while node is not None:

            # if value less than, move to left branch
            if value < node.key:
                prev_node = node
                node = node.left
                direction = 0

            # if value more than, move to right branch
            elif value >= node.key:
                prev_node = node
                node = node.right
                direction = 1

        if direction:
            prev_node.right = Node(value=value)
            return

        prev_node.left = Node(value=value)


    def insert_two(self, node: Node, key: int) -> Node:
        "Node insertion with recursion."

        if node:

            if key < node.key:
                node.left=self.insert_two(node.left, key)

            if key >= node.key:
                node.right=self.insert_two(node.right, key)

        if node is None:
            return Node(key)

        # returns the same node passed by the function
        return node


    def recursive_insert(self, key: int) -> None:
        "Simpler insertion."

        self.insert_two(self.root, key)


    def inorder_traversal(self, node: Node) -> None:
        "To inorder_traversal and print O(n)."

        if node:

            self.inorder_traversal(node.left)
            print(node.key)
            # temp_list.append(node.key)
            self.inorder_traversal(node.right)


    def print_tree(self) -> Node:
        "To print the tree."

        self.inorder_traversal(node=self.root)


    def iterative_search(self, key: int) -> int:
        "To seaarch tree for a key O(n)."

        node = self.root

        while node:

            if key == node.key:
                print(f"Found {key}")
                return

            elif key < node.key:
                node = node.left

            elif key >= node.key:
                node = node.right

        print(f"Not found {key}")
        return


    def find_min(self, node: Node) -> Node:
        "To find the minimum value node."

        while node:
            prev_node = node
            node = node.left

        return prev_node


    def delete_node(self, node: Node, key: int) -> Node:
        "To delete a given node and return root node."

        if node:

            if key < node.key:
                node.left = self.delete_node(node.left, key)

            elif key > node.key:
                node.right = self.delete_node(node.right, key)

            else:
                # when node.key == key run this block
                if node.left is None and node.right is None:
                    return None
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                # when the node has two children
                del_node = self.find_min(node.right)  # find minimum value node on the right subtree
                node.key = del_node.key  # replace current node value with min
                node.right = self.delete_node(node.right, del_node.key)  # delete duplicate on right subtree

            # always return the root node to the subtree in each recursion
            return node

        print(f"Node with key {key} doesn't exist")
        return None  # if node doesn't exist


    def delete(self, value: int) -> None:
        "To delete node."

        self.root = self.delete_node(self.root, value)  # root node is retunrned



# function calls

# first type of insertion
my_tree = BinarySearchTree(8)
my_tree.iterative_insert(5)
my_tree.iterative_insert(5)
my_tree.iterative_insert(4)
my_tree.iterative_insert(6)
my_tree.iterative_insert(6)
my_tree.iterative_insert(7)
my_tree.iterative_insert(11)
my_tree.iterative_insert(22)
my_tree.iterative_insert(1)
my_tree.print_tree()

print()
my_tree.iterative_search(12)

my_tree.delete(5)
my_tree.delete(5)
my_tree.delete(13)
my_tree.delete(8)
my_tree.print_tree()
print(my_tree.root.key)  # root is 11 after deletions

# # second type of insertion using recursion
# my_tree.recursive_insert(5)
# my_tree.recursive_insert(5)
# my_tree.recursive_insert(4)
# my_tree.recursive_insert(6)
# my_tree.print_tree()
