"""Stack data structure implementation in python.

    The usage of stack limit is only to demonstrate
    python stacks with limit. Often python stacks have no limit
    due to the dynamic nature of python list object.

    Best way to create stack with limit is to use class and set the
    attribute for stack size for every stack object.
"""


# standard library import


STACK_LIMIT = 0  # constant

def create_stack(size: int) -> list:
    """To create a stack using list."""

    global STACK_LIMIT
    STACK_LIMIT = size
    stack = []
    return stack

def push(stack: list, item: int) -> None:
    """To add item to the stack."""

    print(len(stack))
    if len(stack) < STACK_LIMIT:
        stack.append(item)
    else:
        print("Stack is full")

def pop(stack: list) -> int:
    """To remove top item and return it."""

    if stack:
        item = stack.pop()
        return item
    else:
        print("The stack is empty")

def peek(stack: list) -> None:
    """To peak the last element in stack."""

    if stack:
        print(stack[-1])
    else:
        print("The stack is empty")

def  IsEmpty(stack: list) -> bool:
    """To checck for empty stack."""

    return len(stack) == 0


# function calls

my_stack = create_stack(4)

# add multiple values to my stack
for i in range(5):
    push(my_stack, i)

# peek the last element
print('\nPeak the stack before popping')
peek(my_stack)

# to pop all element in stack and test beyond limit
print("\nPopping all stack item")
for i in range(6):
    x = pop(my_stack)
    if x is not None:
        print(x)

# to peek last element of empty stack
print('\nPeak the stack after popping')
peek(my_stack)
