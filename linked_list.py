"""
Linked lists implementations in Python.
"""


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append_node(self, value):
        """Appends a value to the end of the linked list."""
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = node

    def get_value(self, index):
        """Returns value at specified index of the linked list."""
        i = 0
        pointer = self.head
        while pointer is not None:
            if i == index:
                return pointer.value
            pointer = pointer.next
            i += 1
        raise IndexError("List index is out of range.")

    def __str__(self):
        out = []
        pointer = self.head
        while pointer is not None:
            out.append(pointer.value)
            pointer = pointer.next
        return out.__str__()


if __name__ == "__main__":

    sll = SinglyLinkedList()
    print(sll)  # Print empty list.

    # Populate linked list.
    array = ['hello', 'world', 1, 52, True]
    for item in array:
        sll.append_node(item)
    print(sll)

    # Get value at index 3 (third item, counting from zero).
    print(sll.get_value(3))
