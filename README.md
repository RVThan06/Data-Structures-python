# Python Data Structures Implementation

A comprehensive, object-oriented library of fundamental data structures built from scratch in Python. This repository serves as a practical reference for understanding the internal mechanics and algorithmic efficiency of classic computer science structures.

---

## 🚀 Overview

This project implements various data structures as Python classes. By avoiding high-level built-in shortcuts, these implementations provide a clear look at memory management, pointer manipulation, and structural logic.

### Key Features:
* **Object-Oriented Design:** Each structure is encapsulated within its own class.
* **Pythonic Implementation:** Includes magic methods like `__iter__` for seamless loops and `__str__` for easy printing.
* **Educational:** Detailed logic for complex operations like index-based insertion and deletion.

---

## 📚 Data Structures Included

### 1. Linear Structures
* **Stack & Queue:** Fundamental LIFO and FIFO implementations.
* **Singly Linked List:** Basic pointer-based linear collection.
* **Doubly Linked List:** Advanced implementation with `prev` and `next` pointers for bidirectional efficiency.


### 2. Tree-Based Structures
* **Binary Search Tree (BST):** Average $O(\log n)$ performance for search/insert.
* **Heap (Min/Max):** Tree-based structure maintaining the heap property.

### 3. Graphs & Hashing
* **Graphs:** Implementations for both **Adjacency Lists** and **Adjacency Matrices**.
* **Hash Table:** Custom key-value mapping with collision resolution.

---

## 💻 Usage Example: Doubly Linked List

Here is how you can use the `LinkedList` class from this library:

```python
from structures.doubly_linked_list import LinkedList

# 1. Initialize the list
ll = LinkedList()

# 2. Insert data at both ends
ll.insert_rear(10)
ll.insert_rear(20)
ll.insert_front(5)  # List: 5 --> 10 --> 20 --> None

# 3. Insert at a specific index
ll.insert_before(new_value=15, index=2)

# 4. Seamlessly iterate through nodes (thanks to __iter__)
for node in ll:
    print(f"Node Data: {node.data}")

# 5. Easy deletion
ll.delete_front()
ll.delete_rear()

# 6. Search for a value
result = ll.search(10)
print(f"Found: {result.data if result else 'Not Found'}")
```
