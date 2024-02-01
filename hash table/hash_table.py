"""
   Hash table implementation in python.
   The hash table only allows unique key,
   With respect to the assumptions made on hash function
   that on average the hash function follows perfect uniform hashing.
   This allows for us to assume the search operation on average is O(1).

   In this prograam built in python hash function is used, other hash functions
   can be used for better performance with uniform hashing

   Thus, insert and delete operation are also O(1) on average.
   This program can be improved by incorporating exception handling when there is
   any unexpected result.

"""


# standard library imports
import linked_list as link


class HashTable:
    """Class to create hash table."""

    def __init__(self, array_length: int) -> None:
        """To initialise hash table with specific array size."""

        self.array = [None] * array_length


    def __iter__(self) -> None:
        """Iterator to iterate the hashmap O(n)."""

        # each iteration yield a list in each hash table slot
        for item in self.array:
            yield item


    def hash_function(self, key: str) -> int:
        """To generate hash function for given key O(1)."""

        index = abs(hash(key)) % len(self.array)
        return index


    def insert(self, key_value: list) -> tuple:
        """To insert a new key-value pair O(1) on average with search at O(1)."""

        index = self.hash_function(key=key_value[0])

        # instatiate list object if slot if empty
        if self.array[index] is None:
            new_list  = link.LinkedList()
            self.array[index] = new_list

        # insert the key if present
        key_status = self.array[index].insert_front(key=key_value[0], value=key_value[1])

        # if failed to insert return key error
        if key_status[0]:
            return f"{key_status[1]} : Key already present"


    def search(self, key: str) -> tuple:
        """To search for a unique key-value pair O(1) on average."""

        index = self.hash_function(key=key)

        # if list slot empty then no linked list
        if self.array[index] is None:
            return (False, "Key doesn't exist")

        # search linked list to check for key and return status
        key_status = self.array[index].search_item(key)
        return key_status


    def delete(self, key: str) -> None:
        """To delete key-value pair if exit O(1) on average."""

        index = self.hash_function(key=key)

        # if list slot empty then no linked list
        if self.array[index] is None:
            return "Key error : Key not present"

        # delete the key if present
        key_status = self.array[index].delete_node(key)

        # if after deletion the list is empty then destroy it and store None
        if key_status[0]:
            if self.array[index].head is None:
                self.array[index] = None
            return f"Key: '{key}' has been deleted"

        # if failed to insert return key error
        if not key_status[0]:
            return f"{key_status[1]} : Key not present"


# function calls

# 1. setting table size
my_table = HashTable(20)

# 2. inserting multiple key-value pairs, each with unique key
my_table.insert(["Arvin", 24])
my_table.insert(['rAvin', 29])
my_table.insert(["Alan", 23])
my_table.insert(["Alex", 27])
my_table.insert(["bfuwb", 33])
my_table.insert(["534t", 26])
my_table.insert(["erdg", 67])
my_table.insert(["htej", 37])
my_table.insert(["kyut", 66])

# 3. print the hashtable
for value in my_table:
    print(value)
print()

# 4. delete keys from hash table
print(my_table.delete("Arvin"))
print(my_table.delete("Ram"))

# 5. print updated hash table
for value in my_table:
    print(value)

# 6. search for a key
status = my_table.search("Alan")
if status:
    print(status[1])
