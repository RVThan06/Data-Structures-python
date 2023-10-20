"""Python file on circular queue data structure implementation in python.

   Circular queue in python indicates that, when items from the beginning
   of queue has been removed new items can be added to the fron upon the
   tail reaching the end.
"""

# standard library imports


class Queue:
    """To create a circular queue object."""

    def __init__(self, length: int) -> None:
        """Initialising attributes"""

        self.length = length
        self.queue = [None] * self.length
        self.head = -1
        self.tail = -1


    def enqueue(self, item: int) -> None:
        """To add item to queue."""

        # check is the queue is full / overflow
        if self.head == (self.tail + 1) % self.length:
            print("The queue is full.")

        # check if the list is empty and append first item
        elif self.head == -1 and self.tail == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
            #print(self.queue)

        else:
            self.tail = (self.tail + 1) % self.length
            self.queue[self.tail] = item
            #print(self.queue)


    def dequeue(self) -> int:
        """To pop the first item in queue."""

        # check if the queue is empty / underflow
        if self.head == -1 and self.tail == -1:
            print("The queue is empty.")

        # check if there's only one element
        elif self.head == self.tail:

            temp = self.queue[self.tail]
            # reset the queue since its empty now
            self.head = -1
            self.tail = -1
            return temp

        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.length
            return temp


# function calls

# create a queue of length 5
my_queue = Queue(5)

# fill the entire queue
for i in range(1,7):
    my_queue.enqueue(i)

# dequeue the entire queue to verify
for i in range(5):
    print(my_queue.dequeue())
